# FeatureReferenceCurve Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~FeatureReferenceCurve`

Obsolete. Superseded by IModelDoc2::FeatureReferenceCurve.
Obsolete. Superseded by [IModelDoc2::FeatureReferenceCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureReferenceCurve.md).

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

Dim instance As IModelDoc
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

*BaseCurves*

*Merge*

*FromFileName*

*ErrorCode*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
