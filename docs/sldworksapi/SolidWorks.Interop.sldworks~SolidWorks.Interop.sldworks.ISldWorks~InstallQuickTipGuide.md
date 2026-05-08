# InstallQuickTipGuide Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~InstallQuickTipGuide`

Implements your add-in's copy of the Quick Tips.
Implements your add-in's copy of the [Quick Tips](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwQuickTip.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub InstallQuickTipGuide( _
   ByVal PInterface As System.Object _
) 
```

```

Dim instance As ISldWorks
Dim PInterface As System.Object
 
instance.InstallQuickTipGuide(PInterface)
```

```

void InstallQuickTipGuide( 
   System.object PInterface
)
```

```

void InstallQuickTipGuide( 
   System.Object^ PInterface
) 
```

#### Parameters

*PInterface*
:   Your add-in's copy of the [Quick Tips](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwQuickTip.md)

Remarks

The name of your add-in's Quick Tips is added to the SOLIDWORKS Help menu. See [ISwQuickTip::MenuName](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwQuickTip~MenuName.md) for details.

See [Quick Tips and Bubble ToopTips](sldworksAPIProgGuide.chm::/OVERVIEW/Quick_Tips_and_Bubble_ToolTips.htm) for for details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::RefreshQuickTipWindow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RefreshQuickTipWindow.md)  
[ISldWorks::UnInstallQuickTipGuide Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UnInstallQuickTipGuide.md)
