# GetFaces Method (ISMCornerReliefData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~GetFaces`

Gets the faces used to create this sheet metal corner.
Gets the faces used to create this sheet metal corner.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetFaces( _
   ByRef Face1 As System.Object, _
   ByRef Face2 As System.Object, _
   ByRef Face3 As System.Object _
) 
```

```

Dim instance As ISMCornerReliefData
Dim Face1 As System.Object
Dim Face2 As System.Object
Dim Face3 As System.Object
 
instance.GetFaces(Face1, Face2, Face3)
```

```

void GetFaces( 
   out System.object Face1,
   out System.object Face2,
   out System.object Face3
)
```

```

void GetFaces( 
   [Out] System.Object^ Face1,
   [Out] System.Object^ Face2,
   [Out] System.Object^ Face3
) 
```

#### Parameters

*Face1*
:   First [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) that defines this two- or three-bend corner

*Face2*
:   Second IFace2 that defines this two- or three-bend corner

*Face3*
:   Third IFace2 that defines this three-bend corner; valid only if ICornerReliefFeatureData::CornerReliefBendType is [swCornerReliefBendType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefBendType_e.html).swCornerReliefBendType\_ThreeBend; specify null or Nothing for a two-bend corner

Example

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMCornerReliefData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.md)  
[ISMCornerReliefData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData_members.md)
