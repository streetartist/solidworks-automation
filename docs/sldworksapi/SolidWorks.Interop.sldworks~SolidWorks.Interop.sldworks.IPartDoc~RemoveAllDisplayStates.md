# RemoveAllDisplayStates Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~RemoveAllDisplayStates`

Removes all display states and appearances from this part document.
Removes all display states and appearances from this part document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveAllDisplayStates() As System.Boolean
```

```

Dim instance As IPartDoc
Dim value As System.Boolean
 
value = instance.RemoveAllDisplayStates()
```

```

System.bool RemoveAllDisplayStates()
```

```

System.bool RemoveAllDisplayStates(); 
```

#### Return Value

True if successful, false if not

Remarks

Call this method to:

- Remove all appearances from all configurations of this part.
- Remove all display states except the active display state.
- Un-link display states from configurations.
- Show all hidden features.

Example

[Clear Display States (VBA)](Clear_Display_States_Example_VB.htm)  
[Clear Display States (VB.NET)](Clear_Display_States_Example_VBNET.htm)  
[Clear Display States (C#)](Clear_Display_States_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IConfigurationManager::LinkDisplayStatesToConfigurations Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~LinkDisplayStatesToConfigurations.md)
