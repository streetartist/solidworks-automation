# FeatureReferenceCurve Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureReferenceCurve`

Creates a reference curve feature from an array of curves.
Creates a reference curve feature from an array of curves.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureReferenceCurve( _
   ByVal NumOfCurves As System.Integer, _
   ByVal BaseCurves As System.Object, _
   ByVal Merge As System.Boolean, _
   ByVal FromFileName As System.String, _
   ByRef ErrorCode As System.Integer _
) As System.Object
```

```

Dim instance As IModelDoc2
Dim NumOfCurves As System.Integer
Dim BaseCurves As System.Object
Dim Merge As System.Boolean
Dim FromFileName As System.String
Dim ErrorCode As System.Integer
Dim value As System.Object
 
value = instance.FeatureReferenceCurve(NumOfCurves, BaseCurves, Merge, FromFileName, ErrorCode)
```

```

System.object FeatureReferenceCurve( 
   System.int NumOfCurves,
   System.object BaseCurves,
   System.bool Merge,
   System.string FromFileName,
   out System.int ErrorCode
)
```

```

System.Object^ FeatureReferenceCurve( 
   System.int NumOfCurves,
   System.Object^ BaseCurves,
   System.bool Merge,
   System.String^ FromFileName,
   [Out] System.int ErrorCode
) 
```

#### Parameters

*NumOfCurves*
:   Number of curves from which to create the object

*BaseCurves*
:   Array of [curves](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurve.md)

*Merge*
:   True creates a single reference curve feature, false creates a reference curve feature for each curve in the array

*FromFileName*
:   Not used

*ErrorCode*
:   Error code as defined in [swFeatureError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureError_e.html)

#### Return Value

[Reference curve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IReferenceCurve.md)

Example

[Create Reference Curve (C#)](Create_Reference_Curve_Example_CSharp.htm)  
[Create Reference Curve (VB.NET)](Create_Reference_Curve_Example_VBNET.htm)  
[Create Reference Curve (VBA)](Create_Reference_Curve_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::IFeatureReferenceCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFeatureReferenceCurve.md)
