# AddNewCorner Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~AddNewCorner`

Adds a corner with the specified parameters to this sheet metal corner relief feature.
Adds a corner with the specified parameters to this sheet metal corner relief feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddNewCorner( _
   ByVal Face1 As System.Object, _
   ByVal Face2 As System.Object, _
   ByVal Face3 As System.Object, _
   ByVal ReliefType As System.Integer, _
   ByRef Corner As System.Object _
) As System.Integer
```

```

Dim instance As ICornerReliefFeatureData
Dim Face1 As System.Object
Dim Face2 As System.Object
Dim Face3 As System.Object
Dim ReliefType As System.Integer
Dim Corner As System.Object
Dim value As System.Integer
 
value = instance.AddNewCorner(Face1, Face2, Face3, ReliefType, Corner)
```

```

System.int AddNewCorner( 
   System.object Face1,
   System.object Face2,
   System.object Face3,
   System.int ReliefType,
   out System.object Corner
)
```

```

System.int AddNewCorner( 
   System.Object^ Face1,
   System.Object^ Face2,
   System.Object^ Face3,
   System.int ReliefType,
   [Out] System.Object^ Corner
) 
```

#### Parameters

*Face1*
:   First [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) that defines this two- or three-bend corner

*Face2*
:   Second IFace2 that defines this two- or three-bend corner

*Face3*
:   Third IFace2 that defines this three-bend corner; valid only if ICornerReliefFeatureData::CornerReliefBendType is [swCornerReliefBendType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefBendType_e.html).swCornerReliefBendType\_ThreeBend; specify null or Nothing for a two-bend corner

*ReliefType*
:   Corner relief type as defined by [swCornerReliefType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefType_e.html)

*Corner*
:   [ISMCornerReliefData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.md)

#### Return Value

Error code as defined by [swCornerReliefError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefError_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICornerReliefFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.md)  
[ICornerReliefFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData_members.md)
