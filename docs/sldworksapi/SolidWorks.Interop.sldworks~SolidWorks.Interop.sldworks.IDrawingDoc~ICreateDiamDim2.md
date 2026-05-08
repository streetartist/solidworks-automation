# ICreateDiamDim2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDiamDim2`

Obsolete. Superseded by IDrawingDoc::ICreateDiamDim4.
Obsolete. Superseded by [IDrawingDoc::ICreateDiamDim4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ICreateDiamDim4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ICreateDiamDim2( _
   ByVal DimValue As System.Double, _
   ByRef P0 As System.Double, _
   ByRef P1 As System.Double, _
   ByRef P2 As System.Double, _
   ByRef P3 As System.Double, _
   ByVal ArrowSize As System.Double, _
   ByVal Text As System.String, _
   ByVal TextHeight As System.Double, _
   ByVal WitnessGap As System.Double, _
   ByVal WitnessOvershoot As System.Double, _
   ByRef TextPoint As System.Double _
) 
```

```

Dim instance As IDrawingDoc
Dim DimValue As System.Double
Dim P0 As System.Double
Dim P1 As System.Double
Dim P2 As System.Double
Dim P3 As System.Double
Dim ArrowSize As System.Double
Dim Text As System.String
Dim TextHeight As System.Double
Dim WitnessGap As System.Double
Dim WitnessOvershoot As System.Double
Dim TextPoint As System.Double
 
instance.ICreateDiamDim2(DimValue, P0, P1, P2, P3, ArrowSize, Text, TextHeight, WitnessGap, WitnessOvershoot, TextPoint)
```

```

void ICreateDiamDim2( 
   System.double DimValue,
   ref System.double P0,
   ref System.double P1,
   ref System.double P2,
   ref System.double P3,
   System.double ArrowSize,
   System.string Text,
   System.double TextHeight,
   System.double WitnessGap,
   System.double WitnessOvershoot,
   ref System.double TextPoint
)
```

```

void ICreateDiamDim2( 
   System.double DimValue,
   System.double% P0,
   System.double% P1,
   System.double% P2,
   System.double% P3,
   System.double ArrowSize,
   System.String^ Text,
   System.double TextHeight,
   System.double WitnessGap,
   System.double WitnessOvershoot,
   System.double% TextPoint
) 
```

#### Parameters

*DimValue*

*P0*

*P1*

*P2*

*P3*

*ArrowSize*

*Text*

*TextHeight*

*WitnessGap*

*WitnessOvershoot*

*TextPoint*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
