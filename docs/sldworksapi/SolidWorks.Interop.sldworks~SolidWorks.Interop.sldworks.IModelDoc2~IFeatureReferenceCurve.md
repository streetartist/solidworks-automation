# IFeatureReferenceCurve Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFeatureReferenceCurve`

Creates a reference curve feature from an array of curves.
Creates a reference curve feature from an array of curves.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IFeatureReferenceCurve( _
   ByVal NumOfCurves As System.Integer, _
   ByRef BaseCurves As Curve, _
   ByVal Merge As System.Boolean, _
   ByVal FromFileName As System.String, _
   ByRef ErrorCode As System.Integer _
) As ReferenceCurve
```

```

Dim instance As IModelDoc2
Dim NumOfCurves As System.Integer
Dim BaseCurves As Curve
Dim Merge As System.Boolean
Dim FromFileName As System.String
Dim ErrorCode As System.Integer
Dim value As ReferenceCurve
 
value = instance.IFeatureReferenceCurve(NumOfCurves, BaseCurves, Merge, FromFileName, ErrorCode)
```

```

ReferenceCurve IFeatureReferenceCurve( 
   System.int NumOfCurves,
   ref Curve BaseCurves,
   System.bool Merge,
   System.string FromFileName,
   out System.int ErrorCode
)
```

```

ReferenceCurve^ IFeatureReferenceCurve( 
   System.int NumOfCurves,
   Curve^% BaseCurves,
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

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::FeatureReferenceCurve Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureReferenceCurve.md)
