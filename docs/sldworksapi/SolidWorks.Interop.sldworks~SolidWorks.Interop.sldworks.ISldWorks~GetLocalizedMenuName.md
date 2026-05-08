# GetLocalizedMenuName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLocalizedMenuName`

Gets a localized menu name for the specified menu ID.
Gets a localized menu name for the specified menu ID.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLocalizedMenuName( _
   ByVal MenuId As System.Integer _
) As System.String
```

```

Dim instance As ISldWorks
Dim MenuId As System.Integer
Dim value As System.String
 
value = instance.GetLocalizedMenuName(MenuId)
```

```

System.string GetLocalizedMenuName( 
   System.int MenuId
)
```

```

System.String^ GetLocalizedMenuName( 
   System.int MenuId
) 
```

#### Parameters

*MenuId*
:   Menu ID as defined in [swMenuIdentifiers\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMenuIdentifiers_e.html)

#### Return Value

String containing the localized menu name

Remarks

The string returned allows the application to provide a correctly localized string representing the menu name that menus and menu items can be when added to in the SOLIDWORKS user interface.

This method should be called before [ISldWorks::AddMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenu.md), [ISldWorks::AddMenuItem3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~AddMenuItem3.md), [IFrame::AddMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenu.md), or [IFrame::AddMenuItem2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~AddMenuItem2.md).

Example

[Get Language and Localized Menu Names (VBA)](Get_Language_and_Localized_Menu_Names_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
