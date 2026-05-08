# SetStyle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetStyle`

Sets the style of the detail circle (for example, standard, broken, leader, no leader, or connected).
Sets the style of the detail circle (for example, standard, broken, leader, no leader, or connected).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetStyle( _
   ByVal Style As System.Integer _
) As System.Boolean
```

```

Dim instance As IDetailCircle
Dim Style As System.Integer
Dim value As System.Boolean
 
value = instance.SetStyle(Style)
```

```

System.bool SetStyle( 
   System.int Style
)
```

```

System.bool SetStyle( 
   System.int Style
) 
```

#### Parameters

*Style*
:   Style as defined by [swDetViewStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDetViewStyle_e.html)

#### Return Value

True if setting the detail view style is successful, false if not

Remarks

This method sets different styles for the detail view display, following the detailing standard, as a broken circle, as a circle or profile with or without a leader to the detail label, or with a line connecting the detail circle or profile with the detail view.

This method automatically load the model for the detail view, if necessary, without prompting the user.

If the style of the detail circle is swDetViewBROKEN or swDetViewSTANDARD and the current detailing standard is ANSI, then this method automatically switches the detail circle or profile display to circle because a broken circle style requires a circle, not a profile.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.md)  
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.md)  
[IDetailCircle::GetStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetStyle.md)
