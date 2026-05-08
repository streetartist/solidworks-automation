# GetInterfaceBrightnessThemeColors Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetInterfaceBrightnessThemeColors`

Gets the theme and colors of the SOLIDWORKS background.
Gets the theme and colors of the SOLIDWORKS background.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetInterfaceBrightnessThemeColors( _
   ByRef Colors As System.Object _
) As System.Integer
```

```

Dim instance As ISldWorks
Dim Colors As System.Object
Dim value As System.Integer
 
value = instance.GetInterfaceBrightnessThemeColors(Colors)
```

```

System.int GetInterfaceBrightnessThemeColors( 
   out System.object Colors
)
```

```

System.int GetInterfaceBrightnessThemeColors( 
   [Out] System.Object^ Colors
) 
```

#### Parameters

*Colors*
:   Array of nine RGB (Red, Green, Blue) decimal values corresponding to the nine color types of the SOLIDWORKS background as defined in [swInterfaceBrightnessColor\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInterfaceBrightnessColor_e.html)

#### Return Value

SOLIDWORKS background theme as defined in [swInterfaceBrightnessTheme\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInterfaceBrightnessTheme_e.html)

Remarks

A SOLIDWORKS add-in can:

- use this method to determine the current theme and colors of the SOLIDWORKS background.
- be notified when the theme and colors in the SOLIDWORKS background change by registering for the [DSldWorksEvents\_InterfaceBrightnessThemeChangeNotifyEventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_InterfaceBrightnessThemeChangeNotifyEventHandler.md) event.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISwHtmlInterface::GetInterfaceBrightnessTheme](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface~GetInterfaceBrightnessTheme.md)
