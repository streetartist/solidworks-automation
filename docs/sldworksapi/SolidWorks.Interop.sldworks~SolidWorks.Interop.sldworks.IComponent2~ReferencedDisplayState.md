# ReferencedDisplayState Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReferencedDisplayState`

Obsolete. Superseded by IComponent2::ReferencedDisplayState2.
Obsolete. Superseded by [IComponent2::ReferencedDisplayState2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReferencedDisplayState2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ReferencedDisplayState As System.String
```

```

Dim instance As IComponent2
Dim value As System.String
 
value = instance.ReferencedDisplayState
```

```

System.string ReferencedDisplayState {get;}
```

```

property System.String^ ReferencedDisplayState {
   System.String^ get();
}
```

#### Property Value

Name of display state

Example

[Get Referenced Display State (VBA)](Get_Referenced_Display_State_Example_VB.htm)  
[Get Referenced Display State (VB.NET)](Get_Referenced_Display_State_Example_VBNET.htm)  
[Get Referenced Display State (C#)](Get_Referenced_Display_State_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IConfiguration::GetDisplayStates Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStates.md)  
[IConfigurationManager::LinkDisplayStatesToConfigurations Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~LinkDisplayStatesToConfigurations.md)
