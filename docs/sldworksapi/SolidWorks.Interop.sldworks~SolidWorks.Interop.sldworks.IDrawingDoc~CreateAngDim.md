# CreateAngDim Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAngDim`

Obsolete. Superseded by IDrawingDoc::CreateAngDim4.
Obsolete. Superseded by [IDrawingDoc::CreateAngDim4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateAngDim4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreateAngDim( _
   ByVal VP0 As System.Object, _
   ByVal VP1 As System.Object, _
   ByVal VP2 As System.Object, _
   ByVal VP3 As System.Object, _
   ByVal VP4 As System.Object, _
   ByVal VP5 As System.Object, _
   ByVal VP6 As System.Object, _
   ByVal ArrowSize As System.Double, _
   ByVal Text As System.String, _
   ByVal TextHeight As System.Double, _
   ByVal WitnessGap As System.Double, _
   ByVal WitnessOvershoot As System.Double _
) As System.Boolean
```

```

Dim instance As IDrawingDoc
Dim VP0 As System.Object
Dim VP1 As System.Object
Dim VP2 As System.Object
Dim VP3 As System.Object
Dim VP4 As System.Object
Dim VP5 As System.Object
Dim VP6 As System.Object
Dim ArrowSize As System.Double
Dim Text As System.String
Dim TextHeight As System.Double
Dim WitnessGap As System.Double
Dim WitnessOvershoot As System.Double
Dim value As System.Boolean
 
value = instance.CreateAngDim(VP0, VP1, VP2, VP3, VP4, VP5, VP6, ArrowSize, Text, TextHeight, WitnessGap, WitnessOvershoot)
```

```

System.bool CreateAngDim( 
   System.object VP0,
   System.object VP1,
   System.object VP2,
   System.object VP3,
   System.object VP4,
   System.object VP5,
   System.object VP6,
   System.double ArrowSize,
   System.string Text,
   System.double TextHeight,
   System.double WitnessGap,
   System.double WitnessOvershoot
)
```

```

System.bool CreateAngDim( 
   System.Object^ VP0,
   System.Object^ VP1,
   System.Object^ VP2,
   System.Object^ VP3,
   System.Object^ VP4,
   System.Object^ VP5,
   System.Object^ VP6,
   System.double ArrowSize,
   System.String^ Text,
   System.double TextHeight,
   System.double WitnessGap,
   System.double WitnessOvershoot
) 
```

#### Parameters

*VP0*

*VP1*

*VP2*

*VP3*

*VP4*

*VP5*

*VP6*

*ArrowSize*

*Text*

*TextHeight*

*WitnessGap*

*WitnessOvershoot*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.md)  
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.md)
