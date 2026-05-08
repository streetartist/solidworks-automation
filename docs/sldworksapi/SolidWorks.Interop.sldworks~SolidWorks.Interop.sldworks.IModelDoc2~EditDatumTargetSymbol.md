# EditDatumTargetSymbol Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditDatumTargetSymbol`

Edits a datum target symbol.
Edits a datum target symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EditDatumTargetSymbol( _
   ByVal Datum1 As System.String, _
   ByVal Datum2 As System.String, _
   ByVal Datum3 As System.String, _
   ByVal AreaStyle As System.Short, _
   ByVal AreaOutside As System.Boolean, _
   ByVal Value1 As System.Double, _
   ByVal Value2 As System.Double, _
   ByVal ValueStr1 As System.String, _
   ByVal ValueStr2 As System.String, _
   ByVal ArrowsSmart As System.Boolean, _
   ByVal ArrowStyle As System.Short, _
   ByVal LeaderLineStyle As System.Short, _
   ByVal LeaderBent As System.Boolean, _
   ByVal ShowArea As System.Boolean, _
   ByVal ShowSymbol As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim Datum1 As System.String
Dim Datum2 As System.String
Dim Datum3 As System.String
Dim AreaStyle As System.Short
Dim AreaOutside As System.Boolean
Dim Value1 As System.Double
Dim Value2 As System.Double
Dim ValueStr1 As System.String
Dim ValueStr2 As System.String
Dim ArrowsSmart As System.Boolean
Dim ArrowStyle As System.Short
Dim LeaderLineStyle As System.Short
Dim LeaderBent As System.Boolean
Dim ShowArea As System.Boolean
Dim ShowSymbol As System.Boolean
Dim value As System.Boolean
 
value = instance.EditDatumTargetSymbol(Datum1, Datum2, Datum3, AreaStyle, AreaOutside, Value1, Value2, ValueStr1, ValueStr2, ArrowsSmart, ArrowStyle, LeaderLineStyle, LeaderBent, ShowArea, ShowSymbol)
```

```

System.bool EditDatumTargetSymbol( 
   System.string Datum1,
   System.string Datum2,
   System.string Datum3,
   System.short AreaStyle,
   System.bool AreaOutside,
   System.double Value1,
   System.double Value2,
   System.string ValueStr1,
   System.string ValueStr2,
   System.bool ArrowsSmart,
   System.short ArrowStyle,
   System.short LeaderLineStyle,
   System.bool LeaderBent,
   System.bool ShowArea,
   System.bool ShowSymbol
)
```

```

System.bool EditDatumTargetSymbol( 
   System.String^ Datum1,
   System.String^ Datum2,
   System.String^ Datum3,
   System.short AreaStyle,
   System.bool AreaOutside,
   System.double Value1,
   System.double Value2,
   System.String^ ValueStr1,
   System.String^ ValueStr2,
   System.bool ArrowsSmart,
   System.short ArrowStyle,
   System.short LeaderLineStyle,
   System.bool LeaderBent,
   System.bool ShowArea,
   System.bool ShowSymbol
) 
```

#### Parameters

*Datum1*
:   Datum reference string 1

*Datum2*
:   Datum reference string 2

*Datum3*
:   Datum reference string 3

*AreaStyle*
:   0 = point, 1 = circle, 2 = rectangle

*AreaOutside*
:   True to display target area dimensions size outside, false otherwise

*Value1*
:   Numeric datum target area diameter or width

*Value2*
:   Numeric datum target area height

*ValueStr1*
:   Value for datum target area diameter or width

*ValueStr2*
:   Value for datum target area height

*ArrowsSmart*
:   True if you want smart arrows, false otherwise

*ArrowStyle*
:   Arrow head style (for example, open, closed, and so on) as defined in [swArrowStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

*LeaderLineStyle*
:   Leaderline type as defined in [swLeaderStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swLeaderStyle_e.html)

*LeaderBent*
:   True if you want a bent leader line, false otherwise

*ShowArea*
:   True if you want to show the target area, false otherwise

*ShowSymbol*
:   True if you want to display the target symbol, false otherwise

#### Return Value

True if datum target symbol is modified, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDocExtension::InsertDatumTargetSymbol2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertDatumTargetSymbol2.md)  
[IDatumTargetSym Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDatumTargetSym.md)
