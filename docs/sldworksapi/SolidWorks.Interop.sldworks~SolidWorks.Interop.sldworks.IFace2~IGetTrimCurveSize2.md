# IGetTrimCurveSize2 Method (IFace2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveSize2`

Gets the size of the array required for IFace2::GetTrimCurves2
Gets the size of the array required for [IFace2::GetTrimCurves2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurves2.md)

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTrimCurveSize2( _
   ByVal WantCubic As System.Integer, _
   ByVal WantNRational As System.Integer _
) As System.Integer
```

```

Dim instance As IFace2
Dim WantCubic As System.Integer
Dim WantNRational As System.Integer
Dim value As System.Integer
 
value = instance.IGetTrimCurveSize2(WantCubic, WantNRational)
```

```

System.int IGetTrimCurveSize2( 
   System.int WantCubic,
   System.int WantNRational
)
```

```

System.int IGetTrimCurveSize2( 
   System.int WantCubic,
   System.int WantNRational
) 
```

#### Parameters

*WantCubic*
:   True if the trim curves are to be cubic, false if not

*WantNRational*
:   True if the trim curves are to be non-rational, false if not

#### Return Value

Size of the array required for IFace2::GetTrimCurves2

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)  
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.md)  
[IFace2::GetTrimCurveTopology Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurveTopology.md)  
[IFace2::GetTrimCurveTopologyCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurveTopologyCount.md)  
[IFace2::GetTrimCurveTopologyTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurveTopologyTypes.md)  
[IFace2::IGetTrimCurveTopology Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveTopology.md)  
[IFace2::IGetTrimCurveTopologyTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveTopologyTypes.md)
