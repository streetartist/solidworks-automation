# ActiveCommandTab Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ActiveCommandTab`

Gets and sets the active SOLIDWORKS CommandManager tab.
Gets and sets the active SOLIDWORKS CommandManager tab.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ActiveCommandTab As System.String
```

```

Dim instance As IModelDocExtension
Dim value As System.String
 
instance.ActiveCommandTab = value
 
value = instance.ActiveCommandTab
```

```

System.string ActiveCommandTab {get; set;}
```

```

property System.String^ ActiveCommandTab {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Active tab name

Example

[Activate SOLIDWORKS CommandManager Tab (VBA)](Activate_SOLIDWORKS_CommandManager_Tab_Example_VB.htm)  
[Activate SOLIDWORKS CommandManager Tab (VB.NET)](Activate_SOLIDWORKS_CommandManager_Tab_Example_VBNET.htm)  
[Activate SOLIDWORKS CommandManager Tab (C#)](Activate_SOLIDWORKS_CommandManager_Tab_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::GetCommandTabs Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCommandTabs.md)  
[IModelDocExtension::ActiveCommandTabIndex Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ActiveCommandTabIndex.md)  
[IModelDocExtension::CommandTabVisible Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CommandTabVisible.md)
