# CreateDiamDim3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDiamDim3`

Obsolete. Superseded by IDrawingDoc::CreateDiamDim4.
Obsolete. Superseded by [IDrawingDoc::CreateDiamDim4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateDiamDim4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateDiamDim3( _
   ByVal DimVal As System.Double, _
   ByVal VP0 As System.Object, _
   ByVal VP1 As System.Object, _
   ByVal VP2 As System.Object, _
   ByVal VP3 As System.Object, _
   ByVal ArrowSize As System.Double, _
   ByVal Text As System.String, _
   ByVal TextHeight As System.Double, _
   ByVal WitnessGap As System.Double, _
   ByVal WitnessOvershoot As System.Double, _
   ByVal VTextPoint As System.Object _
) As System.Object
```

```

Dim instance As IDrawingDoc
Dim DimVal As System.Double
Dim VP0 As System.Object
Dim VP1 As System.Object
Dim VP2 As System.Object
Dim VP3 As System.Object
Dim ArrowSize As System.Double
Dim Text As System.String
Dim TextHeight As System.Double
Dim WitnessGap As System.Double
Dim WitnessOvershoot As System.Double
Dim VTextPoint As System.Object
Dim value As System.Object
 
value = instance.CreateDiamDim3(DimVal, VP0, VP1, VP2, VP3, ArrowSize, Text, TextHeight, WitnessGap, WitnessOvershoot, VTextPoint)
```

```

System.object CreateDiamDim3( 
   System.double DimVal,
   System.object VP0,
   System.object VP1,
   System.object VP2,
   System.object VP3,
   System.double ArrowSize,
   System.string Text,
   System.double TextHeight,
   System.double WitnessGap,
   System.double WitnessOvershoot,
   System.object VTextPoint
)
```

```

System.Object^ CreateDiamDim3( 
   System.double DimVal,
   System.Object^ VP0,
   System.Object^ VP1,
   System.Object^ VP2,
   System.Object^ VP3,
   System.double ArrowSize,
   System.String^ Text,
   System.double TextHeight,
   System.double WitnessGap,
   System.double WitnessOvershoot,
   System.Object^ VTextPoint
) 
```

#### Parameters

*DimVal*

*VP0*

*VP1*

*VP2*

*VP3*

*ArrowSize*

*Text*

*TextHeight*

*WitnessGap*

*WitnessOvershoot*

*VTextPoint*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
