# IFacet Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet`

Allows access to a triangular facet of a mesh or graphics body.
Allows access to a triangular facet of a mesh or graphics body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IFacet 
```

```

Dim instance As IFacet
```

```

public interface IFacet 
```

```

public interface class IFacet 
```

Remarks

For more information about graphics bodies, read the **Graphics Mesh and Mesh BREP Bodies** topic in **SOLIDWORKS user-interface help > Parts and Features**.

Example

'VBA

'===================================================

'Preconditions:

'1. Copy *Public\_Documents***\SOLIDWORKS\SOLIDWORKS 2022\samples\tutorial\api\Part1.PLY** to **c:\temp**.

'2. Open the Immediate window.

'Postconditions:

'1. Press F5 five times, inspecting the Immediate window after each press.

'2. The part is imported first as a graphics body and then as a mesh body.

'3. The macro tests facets, facet edges, and facet vertexes after each import.

'==================================================

Option Explicit

Dim swApp As SldWorks.SldWorks  
Dim swModelDoc As SldWorks.ModelDoc2

Sub main()

    Set swModelDoc = Nothing  
    Set swApp = Application.SldWorks

    TestGraphicsBody  
    TestBodies  
    Set swModelDoc = Nothing  
    swApp.CloseDoc "Part1"  
     
    TestMeshBody  
    TestBodies  
    Set swModelDoc = Nothing  
    swApp.CloseDoc "Part1"

End Sub

Sub TestGraphicsBody()

    Debug.Print "Importing Part1.PLY as a graphics body..."  
    Debug.Print ""  
    Dim boolstatus As Boolean  
    boolstatus = swApp.SetUserPreferenceIntegerValue(swUserPreferenceIntegerValue\_e.swImportStlVrmlModelType, swImportStlVrmlModelType\_e.swImportStlVrmlModelType\_Graphics)  
    boolstatus = swApp.SetUserPreferenceIntegerValue(swUserPreferenceIntegerValue\_e.swImportStlVrmlModelType, 0)

    boolstatus = swApp.LoadFile2("c:\temp\Part1.PLY", "r")  
     
    Set swModelDoc = swApp.ActiveDoc  
    SelectGraphicsBody

End Sub

Sub TestMeshBody()

    Debug.Print "Importing Part1.PLY as a mesh body..."  
    Debug.Print ""  
    Dim boolstatus As Boolean  
    boolstatus = swApp.SetUserPreferenceIntegerValue(swUserPreferenceIntegerValue\_e.swImportStlVrmlModelType, swImportStlVrmlModelType\_e.swImportStlVrmlModelType\_Surface)  
    boolstatus = swApp.SetUserPreferenceIntegerValue(swUserPreferenceIntegerValue\_e.swImportStlVrmlModelType, 1)  
    swApp.SetUserPreferenceToggle swUserPreferenceToggle\_e.swVrmlStlImportAsPSMesh, True

    boolstatus = swApp.LoadFile2("c:\temp\Part1.PLY", "r")  
     
    Set swModelDoc = swApp.ActiveDoc  
    SelectMeshBody

End Sub

Sub SelectGraphicsBody()  
    Stop  
    Debug.Print "Getting the graphics body, Graphic (Closed) -1..."  
    Dim boolstatus As Boolean  
     
    boolstatus = swModelDoc.Extension.SelectByID2("Graphic (Closed) -1", "MESH BODY FEATURE", -9.32538825377272E-02, 0.091, 0.033742378078639, False, 0, Nothing, 0)  
     
    Dim swSelMgr As SldWorks.SelectionMgr  
    Set swSelMgr = swModelDoc.SelectionManager  
     
    Dim lSelType As Long  
    lSelType = swSelMgr.GetSelectedObjectType3(1, -1)  
    If lSelType = swSelGRAPHICSBODY Then  
        Debug.Print "lSelType = swSelGRAPHICSBODY"  
    End If  
     
    Dim swFeature As SldWorks.Feature  
    Set swFeature = swSelMgr.GetSelectedObject6(1, -1)  
     
    If swFeature Is Nothing Then  
        Debug.Print "swFeature is Nothing"  
    ElseIf lSelType = swSelGRAPHICSBODY Then  
        Debug.Print "Select GraphicsBody success"  
        Dim swBody As SldWorks.Body2  
        Set swBody = swFeature.GetSpecificFeature2  
        If swBody Is Nothing Then  
            Debug.Print "swBody Is Nothing"  
        Else  
            Debug.Print "Getting Body success"  
            Dim lBodyType As Long  
            lBodyType = swBody.GetType  
             
            If lBodyType = swconst.swBodyType\_e.swGraphicsBody Then  
                Dim swGraphicsBody As SldWorks.GraphicsBody  
                Set swGraphicsBody = swBody.**GetGraphicsBody**  
                If swGraphicsBody Is Nothing Then  
                    Debug.Print "Graphics body object is Nothing"  
                Else  
                    Debug.Print "GetGraphicsBody success"  
                    Dim swBodyFromGraphics As SldWorks.Body2  
                    Set swBodyFromGraphics = swGraphicsBody.**GetBody**  
                    If swBodyFromGraphics Is Nothing Then  
                        Debug.Print "swGraphicsBody.GetBody failed"  
                    Else  
                        Debug.Print "swGraphicsBody.GetBody success"  
                    End If  
                End If  
            End If  
        End If  
    End If  
     
    Debug.Print "Selecting facet, facet edge, and facet vertex objects in graphics body..."  
     
    swModelDoc.ClearSelection2 True  
    boolstatus = swModelDoc.Extension.SelectByID2("Unknown", "MESHFACETREF", -0.130140285581291, 9.09999999999798E-02, 5.26687725669035E-02, False, 0, Nothing, 0)  
    lSelType = swSelMgr.GetSelectedObjectType3(1, -1)  
    If lSelType = swconst.swSelFACETS Then  
        Debug.Print "Facet selected"  
    Else  
        Debug.Print "Object selected not of type facet"  
    End If  
     
    swModelDoc.ClearSelection2 True  
    boolstatus = swModelDoc.Extension.SelectByID2("Unknown", "MESHFINREF", -7.01858537194084E-02, 9.09999999999798E-02, 5.13894806662165E-02, False, 0, Nothing, 0)  
    lSelType = swSelMgr.GetSelectedObjectType3(1, -1)  
    If lSelType = swSelMESHFACETEDGES Then  
        Debug.Print "Facet edge selected"  
    Else  
        Debug.Print "Object selected not of type facet edge"  
    End If  
     
    swModelDoc.ClearSelection2 True  
    boolstatus = swModelDoc.Extension.SelectByID2("Unknown", "MESHVERTEXREF", -0.117127148857435, 9.09999999999513E-02, 0.099920771345694, False, 0, Nothing, 0)  
    lSelType = swSelMgr.GetSelectedObjectType3(1, -1)  
    If lSelType = swSelMESHFACETVERTICES Then  
        Debug.Print "Facet vertex selected"  
    Else  
        Debug.Print "Object selected not of type facet vertex"  
    End If  
     
    Debug.Print ""  
End Sub

Sub SelectMeshBody()  
    Stop  
    Debug.Print "Getting mesh body, Surface-Imported5..."  
    Dim boolstatus As Boolean  
    ' SW-35234  
    boolstatus = swModelDoc.Extension.SelectByID2("Surface-Imported5", "SURFACEBODY", -9.55822368965755E-02, 9.10000000000082E-02, 3.36061875443647E-02, False, 0, Nothing, 0)  
     
    Dim swSelMgr As SldWorks.SelectionMgr  
    Set swSelMgr = swModelDoc.SelectionManager  
     
    Dim lSelType As Long  
    lSelType = swSelMgr.GetSelectedObjectType3(1, -1)  
    If lSelType = swSelSURFACEBODIES Then  
        Dim swBody As SldWorks.Body2  
        Set swBody = swSelMgr.GetSelectedObject6(1, -1)  
        Dim lBodyType As Long  
        lBodyType = swBody.GetType  
        If lBodyType = swconst.swBodyType\_e.swMeshBody Then  
            Debug.Print "Select MeshBody success"  
            Dim swMeshBody As SldWorks.MeshBody  
            Set swMeshBody = swBody.**GetMeshBody**  
            If swMeshBody Is Nothing Then  
                Debug.Print "Mesh body object is Nothing"  
            Else  
                Debug.Print "Mesh body retrieved"  
                Dim swMBody As SldWorks.Body2  
                Set swMBody = swMeshBody.**GetBody**  
                If swMBody Is Nothing Then  
                    Debug.Print "swMeshBody.GetBody failed"  
                Else  
                    Debug.Print "swMeshBody.GetBody success"  
                End If  
            End If  
        End If  
    End If  
     
    Debug.Print ""  
End Sub

Sub TestBodies()  
    Stop  
    Debug.Print "Testing facets, facet edges, and facet vertexes..."  
    Dim boolstatus As Boolean  
    
    Dim bFilter As Boolean  
    bFilter = swApp.GetSelectionFilter(swSelMESHFACETEDGES)  
    swApp.SetSelectionFilter swSelMESHFACETEDGES, (bFilter = False)  
    bFilter = swApp.GetSelectionFilter(swSelMESHFACETEDGES)

    Dim vFilters As Variant  
    vFilters = swApp.GetSelectionFilters  
    Dim j As Integer  
    
    If Not IsNull(vFilters) Then  
        For j = 0 To UBound(vFilters)  
            Dim lCurFilter As Long  
            lCurFilter = vFilters(j)  
              
            If lCurFilter = swSelGRAPHICSBODY Then  
               Debug.Print "Selection filter is swSelGRAPHICSBODY"  
            ElseIf lCurFilter = swSelFACETS Then  
                Debug.Print "Selection filter is swSelFACETS"  
            ElseIf lCurFilter = swSelMESHFACETEDGES Then  
               Debug.Print "Selection filter is swSelMESHFACETEDGES"  
            ElseIf lCurFilter = swSelMESHFACETVERTICES Then  
               Debug.Print "Selection filter is swSelMESHFACETVERTICES"  
            Else  
               Debug.Print "Selection filter is other than facet/facet edge/facet vertex"  
            End If  
        Next j  
    End If

    Dim lSelFilters(0) As Long  
    Dim vSelFilters As Variant  
    lSelFilters(0) = swSelMESHFACETVERTICES  
    vSelFilters = lSelFilters  
    swApp.SetSelectionFilters vSelFilters, True  
     
    vSelFilters(0) = swSelFACETS  
    swApp.SetSelectionFilters vSelFilters, False  
     
    Dim bApplySelFilters As Boolean  
    bApplySelFilters = swApp.GetApplySelectionFilter  
    Dim bOppSelFilter As Boolean  
    bOppSelFilter = (bApplySelFilters = False)  
    swApp.SetApplySelectionFilter bOppSelFilter  
     
    swApp.SetApplySelectionFilter False  
     
    Set swModelDoc = swApp.ActiveDoc  
    Dim swPartDoc As SldWorks.PartDoc  
    Set swPartDoc = swModelDoc  
     
    Dim vBodies As Variant  
    vBodies = swPartDoc.GetBodies2(-1, False)  
     
    Dim swSelMgr As SldWorks.SelectionMgr  
    Set swSelMgr = swModelDoc.SelectionManager  
    Dim lSelType As Long  
     
    Dim swCurBod As SldWorks.Body2  
    If Not IsEmpty(vBodies) Then  
        Dim i As Integer  
        For i = 0 To UBound(vBodies)  
        Debug.Print ""  
   
            Set swCurBod = vBodies(i)  
             
            Dim lCurBodyType As Long  
            lCurBodyType = swCurBod.GetType  
            If lCurBodyType = swBodyType\_e.swMeshBody Then  
                Debug.Print "Testing mesh body"  
            ElseIf lCurBodyType = swBodyType\_e.swGraphicsBody Then  
                Debug.Print "Testing graphics body"  
            Else  
                Debug.Print "Some other body type"  
            End If  
                 
            swCurBod.Select2 False, Nothing

            swCurBod.DeSelect  
             
            Dim bIsVisible As Boolean  
            bIsVisible = swCurBod.Visible  
            Debug.Print "Visible is " & bIsVisible  
             
            Dim sBodyName As String  
            sBodyName = swCurBod.Name  
            Debug.Print "Name is """ & sBodyName & """"

            Dim bIsMesh As Boolean  
            bIsMesh = swCurBod.**IsMeshBody**  
            Debug.Print "IsMeshBody returned " & bIsMesh  
             
            Dim bIsGraphics As Boolean  
            bIsGraphics = swCurBod.**IsGraphicsBody**  
            Debug.Print "IsGraphicsBody method returned " & bIsGraphics  
             
            Dim swThisMeshBody As SldWorks.MeshBody  
            Set swThisMeshBody = swCurBod.**GetMeshBody** '  
            If swThisMeshBody Is Nothing Then  
                Debug.Print ""  
            Else  
                Dim swThisBodyFromMesh As SldWorks.Body2  
                Set swThisBodyFromMesh = swThisMeshBody.**GetBody**  
                If Not swThisBodyFromMesh Is Nothing Then  
                    Debug.Print "swThisMeshBody.GetBody returned an IBody2."  
                Else  
                    Debug.Print "swThisMeshBody.GetBody returned Nothing."  
                End If  
                 
                Debug.Print "Getting facet, facet edge, and facet vertex objects in this mesh body..."  
                Dim lFacetCount As Long  
                lFacetCount = swThisMeshBody.**GetFacetCount**  
                Debug.Print "Facet count is " & lFacetCount

                Dim vMFacets As Variant  
                vMFacets = swThisMeshBody.**GetFacets**  
                Dim lMFacetIndex As Long  
                For lMFacetIndex = 0 To UBound(vMFacets)  
                    Debug.Print ""  
                    Debug.Print "Facet " & lMFacetIndex + 1  
                    Dim swCurMFacet As SldWorks.Facet  
                    Set swCurMFacet = vMFacets(lMFacetIndex)  
                    Dim swBodyFromCurMFacet As SldWorks.Body2  
                    Set swBodyFromCurMFacet = swCurMFacet.**GetBody**  
                    Dim vEdges As Variant  
                    Dim vVerts As Variant  
                    vEdges = swCurMFacet.**GetFacetEdges**  
                    Dim lEdgesIndex As Long  
                    For lEdgesIndex = 0 To UBound(vEdges)  
                        Dim swCurEdge As SldWorks.Edge  
                        Set swCurEdge = vEdges(lEdgesIndex)  
                        If swCurEdge Is Nothing Then  
                            Debug.Print "Edge object is Nothing"  
                        Else  
                            Debug.Print "Edge retrieved"  
                        End If  
                         
                    Next lEdgesIndex  
                    vVerts = swCurMFacet.**GetFacetVertices**  
                    Dim lVertsIndex As Long  
                    For lVertsIndex = 0 To UBound(vVerts)  
                        Dim swCurVert As SldWorks.Vertex  
                        Set swCurVert = vVerts(lVertsIndex)  
                        If swCurVert Is Nothing Then  
                            Debug.Print "Vertex object is Nothing"  
                        Else  
                            Debug.Print "Vertex retrieved"  
                        End If  
                    Next lVertsIndex  
                    swCurMFacet.Select False, Nothing  
                    lSelType = swSelMgr.GetSelectedObjectType3(1, -1)  
                    If lSelType = swconst.swSelectType\_e.swSelFACETS Then  
                        Debug.Print "Facet selected"  
                    Else  
                        Debug.Print "Object not of type Facet"  
                    End If  
                Next lMFacetIndex  
              
            End If  
                     
            Dim swThisGraphicsBody As SldWorks.GraphicsBody  
            Set swThisGraphicsBody = swCurBod.**GetGraphicsBody**  
            If swThisGraphicsBody Is Nothing Then  
                Debug.Print ""  
            Else  
                Dim swThisBodyFromGraphics As SldWorks.Body2  
                Set swThisBodyFromGraphics = swThisGraphicsBody.**GetBody**  
                If Not swThisBodyFromGraphics Is Nothing Then  
                    Debug.Print "swThisGraphicsBody.GetBody returned an IBody2."  
                Else  
                    Debug.Print "swThisGraphicsBody.GetBody returned Nothing."  
                End If  
                Debug.Print "Getting facet, facet edge, and facet vertex objects in this graphics body..."  
                 
                Dim lGFacetCount As Long  
                lGFacetCount = swThisGraphicsBody.**GetFacetCount**  
                Debug.Print "Facet count is " & lGFacetCount  
                 
                Dim vFacets As Variant  
                vFacets = swThisGraphicsBody.**GetFacets**  
                Dim lFacetIndex As Long  
                For lFacetIndex = 0 To UBound(vFacets)  
                    Debug.Print ""  
                    Debug.Print "Facet " & lFacetIndex + 1  
                    Dim swFacet As SldWorks.Facet  
                    Set swFacet = vFacets(lFacetIndex)  
                    Dim swFacetBody As SldWorks.Body2  
                    Dim swFacetGraphicsBody As GraphicsBody  
                    Set swFacetBody = swFacet.**GetBody**  
                    If swFacetBody Is Nothing Then  
                        Debug.Print "swFacet.GetBody failed"  
                    Else  
                        Debug.Print "swFacet.GetBody returned an IBody2"  
                    End If  
                     
                    Dim vGEdges As Variant  
                    vGEdges = swFacet.**GetFacetEdges**  
                    Dim lFacetEdgesCount As Long  
                    lFacetEdgesCount = UBound(vGEdges) + 1  
                    Dim lFacetEdgesIndex As Long  
                    For lFacetEdgesIndex = 0 To UBound(vGEdges)  
                        Dim swFacetEdge As SldWorks.Edge  
                        Set swFacetEdge = vGEdges(lFacetEdgesIndex)  
                        If swFacetEdge Is Nothing Then  
                            Debug.Print "Edge object is Nothing"  
                        Else  
                            Debug.Print "Edge retrieved"  
                        End If  
                    Next lFacetEdgesIndex  
                     
                    Dim vGVerts As Variant  
                    vGVerts = swFacet.**GetFacetVertices**  
                    Dim lFacetVertsCount As Long  
                    lFacetVertsCount = UBound(vGVerts) + 1  
                    Dim lFacetVertsIndex As Long  
                    For lFacetVertsIndex = 0 To UBound(vGVerts)  
                        Dim swFacetVert As SldWorks.Vertex  
                        Set swFacetVert = vGVerts(lFacetVertsIndex)  
                        If swFacetVert Is Nothing Then  
                            Debug.Print "Vertex object is Nothing"  
                        Else  
                            Debug.Print "Vertex retrieved"  
                        End If

                    Next lFacetVertsIndex  
                     
                    swFacet.Select False, Nothing  
                    lSelType = swSelMgr.GetSelectedObjectType3(1, -1)  
                    If lSelType = swconst.swSelectType\_e.swSelFACETS Then  
                        Debug.Print "Facet selected"  
                    Else  
                        Debug.Print "Object not of type Facet"  
                    End If

                Next lFacetIndex  
                                 
            End If  
        Next i  
    End If  
    Debug.Print ""  
     
    End Sub

Example

[Inspect Facets of Graphics and Mesh Bodies (VB.NET)](Inspect_Facets_Example_VBNET.htm)  
[Inspect Facets of Graphics and Mesh Bodies (C#)](Inspect_Facets_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFacet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
