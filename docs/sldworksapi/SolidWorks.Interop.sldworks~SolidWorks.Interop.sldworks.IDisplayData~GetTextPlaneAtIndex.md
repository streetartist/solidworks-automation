# GetTextPlaneAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextPlaneAtIndex`

Gets the rotation matrix of the specified text relative to the X-Y plane of the model.
Gets the rotation matrix of the specified text relative to the X-Y plane of the model.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetTextPlaneAtIndex( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IDisplayData
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.GetTextPlaneAtIndex(Index)
```

```

System.object GetTextPlaneAtIndex( 
   System.int Index
)
```

```

System.Object^ GetTextPlaneAtIndex( 
   System.int Index
) 
```

#### Parameters

*Index*
:   Zero-based index of the text whose plane rotation matrix to retrieve (see **Remarks**)

#### Return Value

Array of nine doubles of the text plane rotation matrix (see **Remarks**)

Remarks

Use [IDisplayData::GetTextCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextCount.md) to specify Index.

The nine values of the returned rotation matrix (coord(*i*)) are ordered differently from other plane APIs. If you need to manipulate the text plane axes as is shown in the Example section, use the following assignments:

X-axis: coord(0), coord(3), coord(6)

Y-axis: coord(1), coord(4), coord(7)

Z-axis: coord(2), coord(5), coord(8)

Example

'VBA

'Preconditions:

'1. Open a part with three datum annotations in different planes.

'2. Open the Immediate window.

'Postconditions:

'For each datum annotation:

'   1. Prints the text plane rotation matrix.

'   2. Calculates the X-axis of the text plane rotated by the text angle in the XY plane.

'   3. Calculates the cross product of the X- and Z-axis to obtain the new Y-axis.

'   4. Prints the new text plane rotation matrix.

'=======================================

Option Explicit

Dim swApp As SldWorks.SldWorks  
Dim aDoc As ModelDoc2  
Dim aExt As ModelDocExtension  
Dim boolstatus As Boolean  
Dim annotVar As Variant  
Dim i As Integer  
Dim j As Integer  
Dim k As Integer

Sub main()

Set swApp = Application.SldWorks  
Set aDoc = swApp.ActiveDoc  
Set aExt = aDoc.Extension

annotVar = aExt.GetAnnotations()  
If Not IsEmpty(annotVar) Then

    For i = 0 To UBound(annotVar)  
        Dim aAnnot As Annotation  
        Set aAnnot = annotVar(i)  
         
        Dim swDispData As SldWorks.DisplayData  
        Set swDispData = aAnnot.GetDisplayData  
         
        Debug.Print "Number of texts in annotation: " & swDispData.GetTextCount()  
         
        For j = 0 To swDispData.GetTextCount()  
             
            Dim vPlane As Variant  
            vPlane = swDispData.**GetTextPlaneAtIndex**(j)  
              
            If Not (IsEmpty(vPlane)) Then  
                Debug.Print "Text : " & swDispData.GetTextAtIndex(j)  
                ' Normalize very small positive/negative plane array values to 0  
                For k = 0 To 8  
                    If vPlane(k) < 0 Then  
                        If (vPlane(k) > -0.000001) Then  
                            vPlane(k) = 0  
                        End If  
                    ElseIf (vPlane(k) < 0.000001) Then  
                        vPlane(k) = 0  
                    End If  
                Next k  
                     
                Debug.Print "Normalized text plane rotation matrix: "  
                Debug.Print "" & vPlane(0) & " " & vPlane(1) & " " & vPlane(2)  
                Debug.Print "" & vPlane(3) & " " & vPlane(4) & " " & vPlane(5)  
                Debug.Print "" & vPlane(6) & " " & vPlane(7) & " " & vPlane(8)  
                 
                Dim xAxis As Variant  
                Dim yAxis As Variant  
                Dim zAxis As Variant  
                 
                ' The ordering of the array returned by IDisplayData::GetTextPlaneAtIndex differs from other APIs  
                xAxis = Array(vPlane(0), vPlane(3), vPlane(6))  
                yAxis = Array(vPlane(1), vPlane(4), vPlane(7))  
                zAxis = Array(vPlane(2), vPlane(5), vPlane(8))  
                 
                 Dim angle As Double  
                angle = swDispData.GetTextAngleAtIndex(j)  
                 
                ' Rotate xAxis by angle in X-Y plane  
                Dim xAxisNew As Variant  
                xAxisNew = Array(Cos(angle) \* xAxis(0) + Sin(angle) \* yAxis(0), Cos(angle) \* xAxis(1) + Sin(angle) \* yAxis(1), Cos(angle) \* xAxis(2) + Sin(angle) \* yAxis(2))  
                 
                ' Since rotation in the X-Y plane does not change the normal (Z plane),  
                ' take the cross product of X- and Z-axis arrays to get the new Y-axis array (Y = Z CROSS X)  
                yAxis = Array(zAxis(1) \* xAxisNew(2) - zAxis(2) \* xAxisNew(1), -(zAxis(0) \* xAxisNew(2) - zAxis(2) \* xAxisNew(0)), zAxis(0) \* xAxisNew(1) - zAxis(1) \* xAxisNew(0))  
                                
                ' Normalize very small positive/negative axis coordinates to 0  
                For k = 0 To 2  
                    If xAxisNew(k) < 0 Then  
                        If (xAxisNew(k) > -0.000001) Then  
                            xAxisNew(k) = 0  
                        End If  
                    ElseIf (xAxisNew(k) < 0.000001) Then  
                        xAxisNew(k) = 0  
                    End If  
                Next k  
                 
                For k = 0 To 2  
                    If yAxis(k) < 0 Then  
                        If (yAxis(k) > -0.000001) Then  
                            yAxis(k) = 0  
                        End If  
                    ElseIf (yAxis(k) < 0.000001) Then  
                        yAxis(k) = 0  
                    End If  
                Next k  
                 
                For k = 0 To 2  
                    If zAxis(k) < 0 Then  
                        If (zAxis(k) > -0.000001) Then  
                            zAxis(k) = 0  
                        End If  
                    ElseIf (zAxis(k) < 0.000001) Then  
                        zAxis(k) = 0  
                    End If  
                Next k  
                 
                Debug.Print "Normalized text plane matrix after rotation:"  
                Debug.Print "" & xAxisNew(0) & " " & xAxisNew(1) & " " & xAxisNew(2)  
                Debug.Print "" & yAxis(0) & " " & yAxis(1) & " " & yAxis(2)  
                Debug.Print "" & zAxis(0) & " " & zAxis(1) & " " & zAxis(2)  
                 
            End If  
            Debug.Print " "  
        Next j  
    Next i  
End If  
End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData.md)  
[IDisplayData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData_members.md)  
[IAnnotation::GetPlane Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPlane.md)  
[IDisplayData::GetTextAngleAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextAngleAtIndex.md)  
[IDisplayData::GetTextAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextAtIndex.md)  
[IDisplayData::GetTextFontAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextFontAtIndex.md)  
[IDisplayData::GetTextHeightAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextHeightAtIndex.md)  
[IDisplayData::GetTextInBoxHeightAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextInBoxHeightAtIndex.md)  
[IDisplayData::GetTextInBoxStyleAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextInBoxStyleAtIndex.md)  
[IDisplayData::GetTextInBoxWidthAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextInBoxWidthAtIndex.md)  
[IDisplayData::GetTextInvertAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextInvertAtIndex.md)  
[IDisplayData::GetTextLineSpacingAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextLineSpacingAtIndex.md)  
[IDisplayData::GetTextPositionAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextPositionAtIndex.md)  
[IDisplayData::GetTextRefPositionAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayData~GetTextRefPositionAtIndex.md)
