# RefreshQuickTipWindow Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RefreshQuickTipWindow`

Tells the SOLIDWORKS application that your add-in's state has changed and triggers a query for the current URL page.
Tells the SOLIDWORKS application that your add-in's state has changed and triggers a query for the current URL page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub RefreshQuickTipWindow() 
```

```

Dim instance As ISldWorks
 
instance.RefreshQuickTipWindow()
```

```

void RefreshQuickTipWindow()
```

```

void RefreshQuickTipWindow(); 
```

Remarks

See [Quick Tips and Bubble ToopTips](sldworksAPIProgGuide.chm::/OVERVIEW/Quick_Tips_and_Bubble_ToolTips.htm) for for details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::InstallQuickTipGuide Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~InstallQuickTipGuide.md)  
[ISldWorks::UnInstallQuickTipGuide Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UnInstallQuickTipGuide.md)
