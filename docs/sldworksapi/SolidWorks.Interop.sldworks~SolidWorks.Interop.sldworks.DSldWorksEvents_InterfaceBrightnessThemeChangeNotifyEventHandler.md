# DSldWorksEvents_InterfaceBrightnessThemeChangeNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_InterfaceBrightnessThemeChangeNotifyEventHandler`

Notifies an add-in when the SOLIDWORKS background changes.
Notifies an add-in when the SOLIDWORKS background changes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_InterfaceBrightnessThemeChangeNotifyEventHandler( _
   ByVal ThemeType As System.Integer, _
   ByRef Colors As System.Object _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_InterfaceBrightnessThemeChangeNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_InterfaceBrightnessThemeChangeNotifyEventHandler( 
   System.int ThemeType,
   ref System.object Colors
)
```

```

public delegate System.int DSldWorksEvents_InterfaceBrightnessThemeChangeNotifyEventHandler( 
   System.int ThemeType,
   System.Object^% Colors
)
```

#### Parameters

*ThemeType*
:   SOLIDWORKS background as defined in [swInterfaceBrightnessTheme\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInterfaceBrightnessTheme_e.html)

*Colors*
:   Array of RGB (Red, Green, Blue) decimal values (see **Remarks**)

Remarks

The Colors array is indexed by [swInterfaceBrightnessColor\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInterfaceBrightnessColor_e.html).

To get the SOLIDWORKS background:

- theme, use [ISwHtmlInterface::GetInterfaceBrightnessTheme](SolidWorks.Interop.swhtmlcontrol~SolidWorks.Interop.swhtmlcontrol.ISwHtmlInterface~GetInterfaceBrightnessTheme.md).
- theme and colors, [ISldWorks::GetInterfaceBrightnessThemeColors](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetInterfaceBrightnessThemeColors.md).

If developing a C++ application, use [swAppInterfaceBrightnessThemeChangeNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Example

[Add Shortcut Menus to Add-ins (VB.NET)](Add_Shortcut_Menus_to_Add-ins_VBNET.htm)  
[Add Shortcut Menus to Add-ins (C#)](Add_Shortcut_Menus_to_Add-ins_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_InterfaceBrightnessThemeChangeNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_InterfaceBrightnessThemeChangeNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
