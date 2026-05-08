# ConvertToMeshBody Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ConvertToMeshBody`

Converts a solid body to a mesh BREP (boundary representation) body.
Converts a solid body to a mesh BREP (boundary representation) body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ConvertToMeshBody( _
   ByVal GroupFacetsIntoFaces As System.Boolean, _
   ByVal KeepOriginalBody As System.Boolean, _
   ByVal HideOriginalBody As System.Boolean, _
   ByVal MeshRefinement As System.Double, _
   ByVal AdvancedMeshRefinement As System.Boolean, _
   ByVal MaximumDistance As System.Double, _
   ByVal MaximumAngle As System.Double, _
   ByVal DefineMaxElementSize As System.Boolean, _
   ByVal ElementSize As System.Double, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

```

Dim instance As IBody2
Dim GroupFacetsIntoFaces As System.Boolean
Dim KeepOriginalBody As System.Boolean
Dim HideOriginalBody As System.Boolean
Dim MeshRefinement As System.Double
Dim AdvancedMeshRefinement As System.Boolean
Dim MaximumDistance As System.Double
Dim MaximumAngle As System.Double
Dim DefineMaxElementSize As System.Boolean
Dim ElementSize As System.Double
Dim ErrorCode As System.Integer
Dim value As System.Object
 
value = instance.ConvertToMeshBody(GroupFacetsIntoFaces, KeepOriginalBody, HideOriginalBody, MeshRefinement, AdvancedMeshRefinement, MaximumDistance, MaximumAngle, DefineMaxElementSize, ElementSize, ErrorCode)
```

```

System.object ConvertToMeshBody( 
   System.bool GroupFacetsIntoFaces,
   System.bool KeepOriginalBody,
   System.bool HideOriginalBody,
   System.double MeshRefinement,
   System.bool AdvancedMeshRefinement,
   System.double MaximumDistance,
   System.double MaximumAngle,
   System.bool DefineMaxElementSize,
   System.double ElementSize,
   out System.int ErrorCode
)
```

```

System.Object^ ConvertToMeshBody( 
   System.bool GroupFacetsIntoFaces,
   System.bool KeepOriginalBody,
   System.bool HideOriginalBody,
   System.double MeshRefinement,
   System.bool AdvancedMeshRefinement,
   System.double MaximumDistance,
   System.double MaximumAngle,
   System.bool DefineMaxElementSize,
   System.double ElementSize,
   [Out] System.int ErrorCode
) 
```

#### Parameters

*GroupFacetsIntoFaces*
:   True to group facets into multiple faces, false to convert the mesh into a single face; valid only for graphics bodies

*KeepOriginalBody*
:   True to maintain a reference copy of the original solid or surface body; false to not

*HideOriginalBody*
:   True to hide the original body, false to not; valid only of KeepOriginalBody is true

*MeshRefinement*
:   0.0 (larger mesh facets) <= Percent refinement <= 100.0 (smaller mesh facets); valid only if AdvancedMeshRefinement is false

*AdvancedMeshRefinement*
:   True to specify maximum distance and angle, false to not

*MaximumDistance*
:   Maximum distance deviation in meters

*MaximumAngle*
:   Maximum angle deviation in radians

*DefineMaxElementSize*
:   True to specify the maximum length of the fins, false to not

*ElementSize*
:   Length of fins in meters; valid only if DefineMaxElementSize is true

*ErrorCode*
:   0 if successful, -1 if errors

#### Return Value

Array of:

One [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) (if this is a solid body)

 - or -

Multiple surface bodies (if this is a graphics body)

Remarks

Call this method for each body you want to convert.

This method creates **Body-Convert to Mesh Body** in the FeatureManager design tree.

This method is analogous to the **SOLIDWORKS menu Insert > Mesh > Convert To Mesh Body**. For more information, see the **SOLIDWORKS user-interface help > Parts and Features > Graphics Mesh and Mesh BREP Bodies > Converting Solid, Surface or Graphics Bodies to Mesh** topic.

Example

'VBA

'===============================================================  
'Preconditions:  
'1. Open a part that contains a solid body, a graphics body, or a mesh body.  
'2. If you open a solid body, this macro converts it to a mesh body.  
'3. If you open a graphics body that is meshed or you open a mesh body, multi-select the mesh facets that  
'   can be used to create a plane, cylinder, cone, or sphere.  
'4. Open an Immediate window.  
'  
'Postconditions:  
'1. Inspect the Immediate window.  
'2. If a solid body was opened, **Body-Convert to Mesh Body***X* is created in the FeatureManager design tree.  
'3. If a graphics body or a mesh body was opened and you selected facets,  
'   this macro creates a **Surface-From-Mesh***X* feature from the selected mesh facets  
'   using the specified facet tolerance and extend surface size.  
'   If ErrorCodeSurfaceFromMesh is -1, then select more mesh facets and/or  
'   change the IGraphicsBody/IMeshBody::SurfaceFromMesh parameters (SurfaceType/FacetTolerance/ExtendSurfaceSize).  
'===============================================================  
Option Explicit

Sub main()  
    Dim swApp As SldWorks.SldWorks  
    Dim swModelDoc As ModelDoc2  
    Dim swFeatMgr As FeatureManager  
    Dim swSelMgr As SelectionMgr  
    Dim swSelData As SelectData

    Dim boolstatus As Boolean  
    Dim longstatus As Long, longwarnings As Long

    Set swApp = Application.SldWorks  
    Set swModelDoc = swApp.ActiveDoc  
    Set swSelMgr = swModelDoc.SelectionManager  
    Set swSelData = swSelMgr.CreateSelectData  
    swSelData.Mark = 1  
     
    Dim swPartDoc As PartDoc  
    Set swPartDoc = swModelDoc  
    Dim vAllBodies As Variant  
    vAllBodies = swPartDoc.GetBodies2(swAllBodies, False)  
    Dim swGenericBody As Body2  
    Dim lBodyType As Long  
     
    Dim swBody As Body2  
    Dim swGraphicsBody As GraphicsBody  
    Dim swMeshBody As MeshBody  
    Dim swBodyFeat As Feature

    'Use first body that is Solid, Mesh or Graphics Body  
    Set swBody = Nothing  
    Set swMeshBody = Nothing  
    Set swGraphicsBody = Nothing  
    Dim i As Integer  
    For i = 0 To UBound(vAllBodies)  
        Set swGenericBody = vAllBodies(i)  
        lBodyType = swGenericBody.GetType  
        If lBodyType = swBodyType\_e.swSolidBody Then  
            Debug.Print "Body type is swSolidBody"  
            Set swBody = swGenericBody  
            Exit For  
        ElseIf lBodyType = swBodyType\_e.swMeshBody Then  
            Debug.Print "Body type is swMeshBody"  
            Set swBody = swGenericBody  
            Set swMeshBody = swBody.GetMeshBody  
            Exit For  
        ElseIf lBodyType = swBodyType\_e.swGraphicsBody Then  
            Debug.Print "Body type is swGraphicsBody"  
            Set swBody = swGenericBody  
            Set swGraphicsBody = swBody.GetGraphicsBody  
            Exit For  
        End If  
    Next i  
       
    Dim lSelObjType As Long  
    Dim lSelObjCount As Long  
    lSelObjType = swSelMgr.GetSelectedObjectType3(1, -1)  
     
    If lSelObjType = swSelNOTHING Then  
        Debug.Print "Nothing is selected"  
    ElseIf lSelObjType = swSelSOLIDBODIES Then  
        Debug.Print "swSolidBody is selected"  
    ElseIf lSelObjType = swSelGRAPHICSBODY Then  
        Debug.Print "swGraphicsBody is selected"  
    ElseIf lSelObjType = swSelMESHSOLIDBODIES Then  
        Debug.Print "swMeshBody is selected"  
    ElseIf lSelObjType = swSelFACETS Then  
        Debug.Print "swSelFACETS is selected"  
    Else  
        Debug.Print "Nothing interesting is selected"  
    End If

    Dim swSurfaceBody As Body2  
    Dim SurfaceType As Long  
    Dim FacetTolerance As Double  
    Dim ExtendSurfaceSize As Double  
    Dim ErrorCodeSurfaceFromMesh As Long  
    Set swSurfaceBody = Nothing  
    SurfaceType = swSurfaceTypes\_e.PLANE\_TYPE  
    FacetTolerance = 0  
    ExtendSurfaceSize = 0.023  
    ErrorCodeSurfaceFromMesh = 0

    If Not swGraphicsBody Is Nothing Then  'And lSelObjType = swSelFACETS  
        Debug.Print "Testing GraphicsBody.SurfaceFromMesh"  
        Set swSurfaceBody = swGraphicsBody.**SurfaceFromMesh**(SurfaceType, FacetTolerance, ExtendSurfaceSize, ErrorCodeSurfaceFromMesh)  
        Debug.Print "ErrorCodeSurfaceFromMesh = " & ErrorCodeSurfaceFromMesh  
    ElseIf Not swMeshBody Is Nothing Then 'And lSelObjType = swSelFACETS  
        Debug.Print "Testing MeshBody.SurfaceFromMesh"  
        Set swSurfaceBody = swMeshBody.**SurfaceFromMesh**(SurfaceType, FacetTolerance, ExtendSurfaceSize, ErrorCodeSurfaceFromMesh)  
        Debug.Print "ErrorCodeSurfaceFromMesh = " & ErrorCodeSurfaceFromMesh  
    ElseIf Not swBody Is Nothing Then  
        Debug.Print "Testing ConvertToMeshBody"  
        swBody.Select2 False, swSelData  
        Dim outBodiesArray As Variant  
        Dim GroupFacetsIntoFaces As Boolean  
        Dim KeepOriginalBody As Boolean  
        Dim HideOriginalBody As Boolean  
        Dim MeshRefinement As Double  
        Dim AdvancedMeshRefinement As Boolean  
        Dim MaximumDistance As Double  
        Dim MaximumAngle As Double  
        Dim DefineMaxElementSize As Boolean  
        Dim ElementSize As Double  
        Dim ErrorCode As Long  
        GroupFacetsIntoFaces = False  
        KeepOriginalBody = False  
        HideOriginalBody = False  
        MeshRefinement = 0.005  
        AdvancedMeshRefinement = False  
        MaximumDistance = 0.01  
        MaximumAngle = 0.05  
        DefineMaxElementSize = False  
        ElementSize = 0.01  
        ErrorCode = -1  
        outBodiesArray = swBody.**ConvertToMeshBody**(GroupFacetsIntoFaces, KeepOriginalBody, HideOriginalBody, MeshRefinement, AdvancedMeshRefinement, MaximumDistance, MaximumAngle, DefineMaxElementSize, ElementSize, ErrorCode)  
        If IsEmpty(outBodiesArray) Then  
            Debug.Print "outBodiesArray is Empty"  
        Else  
            Dim lCount As Long  
            lCount = UBound(outBodiesArray) - LBound(outBodiesArray) + 1  
            If lCount > 0 Then  
                Debug.Print "outBodiesArray has " & lCount & " elements."  
                Dim swNewBody As Body2  
                Set swNewBody = outBodiesArray(0)  
                If Not swNewBody Is Nothing Then  
                    Debug.Print "Returned a Body"  
                Else  
                    Debug.Print "No Body Returned"  
                End If  
            Else  
               Debug.Print "outBodiesArray has no elements."  
            End If  
        End If  
        Debug.Print "ErrorCodeConvertToMesh = " & ErrorCode  
    End If  
     
End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
