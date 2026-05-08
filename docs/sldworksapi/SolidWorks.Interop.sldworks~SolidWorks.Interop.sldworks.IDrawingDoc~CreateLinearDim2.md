# CreateLinearDim2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateLinearDim2`

Obsolete. Superseded by IDrawingDoc::CreateLinearDim4.
Obsolete. Superseded by [IDrawingDoc::CreateLinearDim4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateLinearDim4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateLinearDim2( _
   ByVal P0 As System.Object, _
   ByVal P1 As System.Object, _
   ByVal P2 As System.Object, _
   ByVal P3 As System.Object, _
   ByVal P4 As System.Object, _
   ByVal Val As System.Double, _
   ByVal PrimPrec As System.Integer, _
   ByVal Text As System.String, _
   ByVal TextPoint As System.Object, _
   ByVal Angle As System.Double, _
   ByVal TextHeight As System.Double, _
   ByVal Prefix As System.String, _
   ByVal Suffix As System.String, _
   ByVal Callout1 As System.String, _
   ByVal Callout2 As System.String, _
   ByVal TolType As System.Integer, _
   ByVal TolMin As System.String, _
   ByVal TolMax As System.String, _
   ByVal TolPrec As System.Integer, _
   ByVal ArrowSize As System.Double, _
   ByVal ArrowStyle As System.Integer, _
   ByVal ArrowDir As System.Integer, _
   ByVal WitnessGap As System.Double, _
   ByVal WitnessOvershoot As System.Double, _
   ByVal DualDisplay As System.Boolean, _
   ByVal DualPrec As System.Integer _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim P0 As System.Object
Dim P1 As System.Object
Dim P2 As System.Object
Dim P3 As System.Object
Dim P4 As System.Object
Dim Val As System.Double
Dim PrimPrec As System.Integer
Dim Text As System.String
Dim TextPoint As System.Object
Dim Angle As System.Double
Dim TextHeight As System.Double
Dim Prefix As System.String
Dim Suffix As System.String
Dim Callout1 As System.String
Dim Callout2 As System.String
Dim TolType As System.Integer
Dim TolMin As System.String
Dim TolMax As System.String
Dim TolPrec As System.Integer
Dim ArrowSize As System.Double
Dim ArrowStyle As System.Integer
Dim ArrowDir As System.Integer
Dim WitnessGap As System.Double
Dim WitnessOvershoot As System.Double
Dim DualDisplay As System.Boolean
Dim DualPrec As System.Integer
Dim value As System.Boolean
 
value = instance.CreateLinearDim2(P0, P1, P2, P3, P4, Val, PrimPrec, Text, TextPoint, Angle, TextHeight, Prefix, Suffix, Callout1, Callout2, TolType, TolMin, TolMax, TolPrec, ArrowSize, ArrowStyle, ArrowDir, WitnessGap, WitnessOvershoot, DualDisplay, DualPrec)
```

```

System.bool CreateLinearDim2( 
   System.object P0,
   System.object P1,
   System.object P2,
   System.object P3,
   System.object P4,
   System.double Val,
   System.int PrimPrec,
   System.string Text,
   System.object TextPoint,
   System.double Angle,
   System.double TextHeight,
   System.string Prefix,
   System.string Suffix,
   System.string Callout1,
   System.string Callout2,
   System.int TolType,
   System.string TolMin,
   System.string TolMax,
   System.int TolPrec,
   System.double ArrowSize,
   System.int ArrowStyle,
   System.int ArrowDir,
   System.double WitnessGap,
   System.double WitnessOvershoot,
   System.bool DualDisplay,
   System.int DualPrec
)
```

```

System.bool CreateLinearDim2( 
   System.Object^ P0,
   System.Object^ P1,
   System.Object^ P2,
   System.Object^ P3,
   System.Object^ P4,
   System.double Val,
   System.int PrimPrec,
   System.String^ Text,
   System.Object^ TextPoint,
   System.double Angle,
   System.double TextHeight,
   System.String^ Prefix,
   System.String^ Suffix,
   System.String^ Callout1,
   System.String^ Callout2,
   System.int TolType,
   System.String^ TolMin,
   System.String^ TolMax,
   System.int TolPrec,
   System.double ArrowSize,
   System.int ArrowStyle,
   System.int ArrowDir,
   System.double WitnessGap,
   System.double WitnessOvershoot,
   System.bool DualDisplay,
   System.int DualPrec
) 
```

#### Parameters

*P0*

*P1*

*P2*

*P3*

*P4*

*Val*

*PrimPrec*

*Text*

*TextPoint*

*Angle*

*TextHeight*

*Prefix*

*Suffix*

*Callout1*

*Callout2*

*TolType*

*TolMin*

*TolMax*

*TolPrec*

*ArrowSize*

*ArrowStyle*

*ArrowDir*

*WitnessGap*

*WitnessOvershoot*

*DualDisplay*

*DualPrec*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
