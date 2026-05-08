# ShowThirdPartyPopupMenu Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ShowThirdPartyPopupMenu`

Sets where to show a third-party pop-up (shortcut) menu.
Sets where to show a third-party pop-up (shortcut) menu.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ShowThirdPartyPopupMenu( _
   ByVal RegisterId As System.Integer, _
   ByVal Posx As System.Integer, _
   ByVal Posy As System.Integer _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim RegisterId As System.Integer
Dim Posx As System.Integer
Dim Posy As System.Integer
Dim value As System.Boolean
 
value = instance.ShowThirdPartyPopupMenu(RegisterId, Posx, Posy)
```

```

System.bool ShowThirdPartyPopupMenu( 
   System.int RegisterId,
   System.int Posx,
   System.int Posy
)
```

```

System.bool ShowThirdPartyPopupMenu( 
   System.int RegisterId,
   System.int Posx,
   System.int Posy
) 
```

#### Parameters

*RegisterId*
:   ID of shortcut menu from [ISldWorks::RegisterThirdPartyPopupMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RegisterThirdPartyPopupMenu.md)

*Posx*
:   x coordinate for shortcut menu

*Posy*
:   y coordinate for shortcut menu

#### Return Value

True to show shortcut menu, false to not

Remarks

Read about [Add-in Shortcut Menus](ms-its:sldworksapiprogguide.chm::/OVERVIEW/Add-in_Shortcut_Menus.htm).

Example

[Add Shortcut Menus to Add-ins (VB.NET)](Add_Shortcut_Menus_to_Add-ins_VBNET.htm)  
[Add Shortcut Menus to Add-ins (C#)](Add_Shortcut_Menus_to_Add-ins_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
