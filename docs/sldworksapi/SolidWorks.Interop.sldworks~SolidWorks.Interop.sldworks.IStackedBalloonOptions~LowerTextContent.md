# LowerTextContent Property (IStackedBalloonOptions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~LowerTextContent`

Gets and sets the style of the lower text of the balloons.
Gets and sets the style of the lower text of the balloons.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LowerTextContent As System.Integer
```

```

Dim instance As IStackedBalloonOptions
Dim value As System.Integer
 
instance.LowerTextContent = value
 
value = instance.LowerTextContent
```

```

System.int LowerTextContent {get; set;}
```

```

property System.int LowerTextContent {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Style of the lower text of the balloons as defined in [swBalloonTextContent\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html); specify -1 to use the document default lower text style (see **Remarks**)

Remarks

This property is valid only when [IStackedBalloonOptions::Style](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~Style.md) is set to [swBalloonStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonStyle_e.html).swBS\_SplitCirc.

|  |  |
| --- | --- |
| To get or set document default values for LowerTextContent... | Use... |
| Get | [IModelDocExtension::GetUserPreferenceInteger](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.md)(swUserPreferenceIntegerValue\_e.swDetailingBOMLowerText, swUserPreferenceOption\_e.swDetailingNoOptionSpecified) |
| Set | [IModelDocExtension::SetUserPreferenceInteger](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceInteger.md)(swUserPreferenceIntegerValue\_e.swDetailingBOMLowerText, swUserPreferenceOption\_e.swDetailingNoOptionSpecified, swBalloonTextContent\_e.<Value>) |

See the SOLIDWORKS Help for additional details about stacked balloons.

Example

See [IStackedBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.md)  
[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.md)
