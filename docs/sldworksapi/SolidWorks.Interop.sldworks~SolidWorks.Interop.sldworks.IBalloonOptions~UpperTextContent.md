# UpperTextContent Property (IBalloonOptions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions~UpperTextContent`

Gets and sets the style of the upper text of the balloon.
Gets and sets the style of the upper text of the balloon.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UpperTextContent As System.Integer
```

```

Dim instance As IBalloonOptions
Dim value As System.Integer
 
instance.UpperTextContent = value
 
value = instance.UpperTextContent
```

```

System.int UpperTextContent {get; set;}
```

```

property System.int UpperTextContent {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Style of the upper text as defined in [swBalloonTextContent\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonTextContent_e.html); specify -1 to use the document default upper text style (see **Remarks**)

Remarks

|  |  |
| --- | --- |
| To get or set document default values... | Use... |
| Get | [IModelDocExtension::GetUserPreferenceInteger](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.md)(swUserPreferenceIntegerValue\_e.swDetailingBOMUpperText, swUserPreferenceOption\_e.swDetailingNoOptionSpecified) |
| Set | [IModelDocExtension::SetUserPreferenceInteger](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceInteger.md)(swUserPreferenceIntegerValue\_e.swDetailingBOMUpperText, swUserPreferenceOption\_e.swDetailingNoOptionSpecified, swBalloonTextContent\_e.<Value>) |

See:

- [INote::PropertyLinkedText](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~PropertyLinkedText.md) for examples of link strings usable with swBalloonTextContent\_e.swBalloonTextCustomProperties.
- SOLIDWORKS Help for additional details about balloons.

Example

See [IBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.md)  
[IBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions_members.md)
