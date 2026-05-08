# ReferencedDisplayState2 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReferencedDisplayState2`

Gets or sets the active display state of this component.
Gets or sets the active display state of this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReferencedDisplayState2 As System.String
```

```

Dim instance As IComponent2
Dim value As System.String
 
instance.ReferencedDisplayState2 = value
 
value = instance.ReferencedDisplayState2
```

```

System.string ReferencedDisplayState2 {get; set;}
```

```

property System.String^ ReferencedDisplayState2 {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Name of display state

Example

[Set Active Display State of Referenced Component (C#)](Set_Active_Display_State_of_Referenced_Component_Example_CSharp.htm)  
[Set Active Display State of Referenced Component (VB.NET)](Set_Active_Display_State_of_Referenced_Component_Example_VBNET.htm)  
[Set Active Display State of Referenced Component (VBA)](Set_Active_Display_State_of_Referenced_Component_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IConfiguration::GetDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetDisplayStates.md)  
[IConfigurationManager::LinkDisplayStatesToConfigurations Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfigurationManager~LinkDisplayStatesToConfigurations.md)
