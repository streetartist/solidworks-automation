# Evaluate2 Method (ICurve)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Evaluate2`

Evaluates the curve at the specified parameter of the curve.
Evaluates the curve at the specified parameter of the curve.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Evaluate2( _
   ByVal Parameter As System.Double, _
   ByVal NumberOfDerivatives As System.Integer _
) As System.Object
```

```

Dim instance As ICurve
Dim Parameter As System.Double
Dim NumberOfDerivatives As System.Integer
Dim value As System.Object
 
value = instance.Evaluate2(Parameter, NumberOfDerivatives)
```

```

System.object Evaluate2( 
   System.double Parameter,
   System.int NumberOfDerivatives
)
```

```

System.Object^ Evaluate2( 
   System.double Parameter,
   System.int NumberOfDerivatives
) 
```

#### Parameters

*Parameter*
:   Curve parameter U value (see **Remarks**)

*NumberOfDerivatives*
:   Number of derivatives (see **Remarks**)

#### Return Value

Array of doubles (see Remarks)

Remarks

To determine the valid range of U parameter values for Parameter, use [ICurve::GetEndParams](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetEndParams.md) or [IEdge::GetCurveParams3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetCurveParams3.md).

The returned array contains ((NumberOfDerivatives + 1) \* 3) + 1 doubles:

[evaluated\_point], [evaluated\_derivative\_1],...[evaluated\_derivative\_NumberOfDerivatives, **[***status\_code***]**

where *status\_code* is a packed double. After unpacking *status\_code* into two longs, the lower long value is 1 for success or 0 for error. See the Example.

In terms of the number of derivatives that can be returned for a curve type:

|  |  |
| --- | --- |
| If curve type [ICurve::Identity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~Identity.md) is... | Then the maximum number of derivatives is... |
| Line/circle/ellipse | 2 |
| Intersection curve | 2 |
| Constant parameter line | Determined by underlying surface |
| SP-curve | 2 |
| B-curve | Any number |

For a curve of type swCurveTypes\_e::TRIMMED\_TYPE, the number of derivatives is determined by the base curve as obtained from [ICurve::GetBaseCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve~GetBaseCurve.md).

Example

1. Open a part in SOLIDWORKS.
2. Open an Immediate window.
3. Select an edge.
4. Run this VBA macro:

```

'=========================================================
```

```

Option Explicit
```

```

Dim swApp As SldWorks.SldWorks  
Dim Part As SldWorks.ModelDoc2  
Dim boolstatus As BooleanDim longstatus As Long, longwarnings As Long
```

```

Type DoubleRec     
     dValue As Double '64 bits, 8 bytes  
End Type
```

```

Type Int2Rec   
     iLower As Long '4 bytes   
     iUpper As Long '4 bytes  
End Type
```

```

' Unpack the status double  
Function DoubleToLong(ByVal dVal As Double) As Long   
    Dim dr As DoubleRec   
    Dim i2r As Int2Rec   
    ' Set the double value   
    dr.dValue = dVal   
    ' Copy the values   
    LSet i2r = dr   
    ' Extract the status value   
    DoubleToLong = i2r.iLower  
End Function
```

```

Sub main()
```

```

    Dim status As Long  
    Set swApp = Application.SldWorks    
    Set Part = swApp.ActiveDoc   
    Dim myModelView As SldWorks.ModelView  
    Set myModelView = Part.ActiveView   
    myModelView.FrameState = swWindowState_e.swWindowMaximized     
    Dim swSelectMgr As SldWorks.SelectionMgr  
    Set swSelectMgr = Part.SelectionManager   
    Dim swEdge As SldWorks.Edge  
    Set swEdge = swSelectMgr.GetSelectedObject6(1, -1)    
    Dim swCurve As SldWorks.Curve   
    Dim swCurveParamData As SldWorks.CurveParamData   
    Set swCurve = swEdge.GetCurve   
    Set swCurveParamData = swEdge.GetCurveParams3    
    Debug.Print "The maximum U parameter value is: " & swCurveParamData.UMaxValue   
    Debug.Print "The minimum U parameter value is: " & swCurveParamData.UMinValue    
    Dim pt As Variant   
    pt = swCurve.Evaluate2(swCurveParamData.UMaxValue, 0)   
    status = DoubleToLong(pt(UBound(pt)))   
    If status Then     
        Debug.Print " The evaluated point at UMax is:   = " & pt(0) & ", " & pt(1) & ", " & pt(2)   
    Else     
        Debug.Print "***** Error!"   
    End If
```

```

End Sub  
'====================================================================
```

Example

[Create Trimmed Curve (VBA)](Return_Untrimmed_Curve_Example_VB.htm)  
[Create Trimmed Curve (VB.NET)](Return_Untrimmed_Curve_Example_VBNET.htm)  
[Create Trimmed Curve (C#)](Return_Untrimmed_Curve_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurve Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)  
[ICurve Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve_members.md)
