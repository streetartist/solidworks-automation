# Size Property (IAutoBalloonOptions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~Size`

Gets and sets the size of the balloons.
Gets and sets the size of the balloons.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Size As System.Integer
```

```

Dim instance As IAutoBalloonOptions
Dim value As System.Integer
 
instance.Size = value
 
value = instance.Size
```

```

System.int Size {get; set;}
```

```

property System.int Size {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Size of the balloons as defined in [swBalloonFit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonFit_e.html); specify -1 to use the document default balloon size (see **Remarks**)

Remarks

|  |  |
| --- | --- |
| To get or set document default values for Size... | Use... |
| Get | [IModelDocExtension::GetUserPreferenceInteger](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetUserPreferenceInteger.md)((swUserPreferenceIntegerValue\_e.swDetailingBOMBalloonFit, swUserPreferenceOption\_e.swDetailingNoOptionSpecified) |
| Set | [IModelDocExtension::SetUserPreferenceInteger](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetUserPreferenceInteger.md)  (swUserPreferenceIntegerValue\_e.swDetailingBOMBalloonFit, swUserPreferenceOption\_e.swDetailingNoOptionSpecified, swBalloonFit\_e.<Value>) |

See the SOLIDWORKS Help for additional details about autoballoons.

Example

See [IAutoBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.md)  
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.md)
