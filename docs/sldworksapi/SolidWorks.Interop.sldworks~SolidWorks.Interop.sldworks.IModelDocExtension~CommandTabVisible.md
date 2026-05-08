# CommandTabVisible Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CommandTabVisible`

Gets and sets the visibility of the specified SOLIDWORKS CommandManager tab.
Gets and sets the visibility of the specified SOLIDWORKS CommandManager tab.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CommandTabVisible( _
   ByVal TabIndex As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim TabIndex As System.Integer
Dim value As System.Boolean
 
instance.CommandTabVisible(TabIndex) = value
 
value = instance.CommandTabVisible(TabIndex)
```

```

System.bool CommandTabVisible( 
   System.int TabIndex
) {get; set;}
```

```

property System.bool CommandTabVisible {
   System.bool get(System.int TabIndex);
   void set (System.int TabIndex, System.bool value);
}
```

#### Parameters

*TabIndex*
:   Index of the tab for which to get or set visibility

#### Property Value

True to make the tab visible, false to not

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
[IModelDocExtension::ActiveCommandTab Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ActiveCommandTab.md)  
[IModelDocExtension::ActiveCommandTabIndex Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ActiveCommandTabIndex.md)  
[IModelDocExtension::GetCommandTabs Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCommandTabs.md)
