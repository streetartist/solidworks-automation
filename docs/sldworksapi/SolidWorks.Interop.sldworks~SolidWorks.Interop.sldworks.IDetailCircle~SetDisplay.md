# SetDisplay Method (IDetailCircle)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetDisplay`

Sets the display of the detail circle to a circle or to the profile.
Sets the display of the detail circle to a circle or to the profile.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetDisplay( _
   ByVal Display As System.Integer _
) As System.Boolean
```

```

Dim instance As IDetailCircle
Dim Display As System.Integer
Dim value As System.Boolean
 
value = instance.SetDisplay(Display)
```

```

System.bool SetDisplay( 
   System.int Display
)
```

```

System.bool SetDisplay( 
   System.int Display
) 
```

#### Parameters

*Display*
:   Display as defined by [swDetCircleShowType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDetCircleShowType_e.html)

#### Return Value

True if setting the detail circle display is successful, false if not

Remarks

Use this method to display the detail circle or detail profile as a circle or as a profile.

|  |  |
| --- | --- |
| **If...** | **Then...** |
| Detail circle was originally set up as a circle | - there is no profile. - using this method to set display to swDetCirclePROFILE has no effect. - this method returns false. |
| Style of the detail circle (see [IDetailCircle::GetStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetStyle.md)) is swDetViewBROKEN or swDetViewSTANDARD  and the current detailing standard is ANSI | this method cannot set the display to swDetCirclePROFILE because the display must  be a circle. |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.md)  
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.md)  
[IDetailCircle::GetStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~GetStyle.md)
