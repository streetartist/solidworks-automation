# IFeatureReferenceCurve Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~IFeatureReferenceCurve`

Obsolete. Superseded by IModelDoc2::IFeatureReferenceCurve.
Obsolete. Superseded by [IModelDoc2::IFeatureReferenceCurve](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IFeatureReferenceCurve.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IFeatureReferenceCurve( _
   ByVal NumOfCurves As System.Integer, _
   ByVal BaseCurves As System.IntPtr, _
   ByVal Merge As System.Boolean, _
   ByVal FromFileName As System.String, _
   ByRef ErrorCode As System.Integer _
) As ReferenceCurve
```

```

Dim instance As IModelDoc
Dim NumOfCurves As System.Integer
Dim BaseCurves As System.IntPtr
Dim Merge As System.Boolean
Dim FromFileName As System.String
Dim ErrorCode As System.Integer
Dim value As ReferenceCurve
 
value = instance.IFeatureReferenceCurve(NumOfCurves, BaseCurves, Merge, FromFileName, ErrorCode)
```

```

ReferenceCurve IFeatureReferenceCurve( 
   System.int NumOfCurves,
   System.IntPtr BaseCurves,
   System.bool Merge,
   System.string FromFileName,
   out System.int ErrorCode
)
```

```

ReferenceCurve^ IFeatureReferenceCurve( 
   System.int NumOfCurves,
   System.IntPtr BaseCurves,
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
