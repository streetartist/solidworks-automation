# UnInstallQuickTipGuide Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UnInstallQuickTipGuide`

Uninstalls your add-in's Quick Tips
Uninstalls your add-in's [Quick Tips](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwQuickTip.md)

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub UnInstallQuickTipGuide( _
   ByVal PInterface As System.Object _
) 
```

```

Dim instance As ISldWorks
Dim PInterface As System.Object
 
instance.UnInstallQuickTipGuide(PInterface)
```

```

void UnInstallQuickTipGuide( 
   System.object PInterface
)
```

```

void UnInstallQuickTipGuide( 
   System.Object^ PInterface
) 
```

#### Parameters

*PInterface*
:   Your add-in's [Quick Tips](SOLIDWORKS.Interop.swpublished~SOLIDWORKS.Interop.swpublished.ISwQuickTip.md)

Remarks

See [Quick Tips and Bubble ToopTips](sldworksAPIProgGuide.chm::/OVERVIEW/Quick_Tips_and_Bubble_ToolTips.htm) for for details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::RefreshQuickTipWindow Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RefreshQuickTipWindow.md)  
[ISldWorks::InstallQuickTipGuide Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~InstallQuickTipGuide.md)
