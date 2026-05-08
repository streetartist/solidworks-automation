# DisplayTitle Property (IModelDocExtension)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DisplayTitle`

Gets and sets this model's title to display in the FeatureManager design tree.
Gets and sets this model's title to display in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DisplayTitle As System.String
```

```

Dim instance As IModelDocExtension
Dim value As System.String
 
instance.DisplayTitle = value
 
value = instance.DisplayTitle
```

```

System.string DisplayTitle {get; set;}
```

```

property System.String^ DisplayTitle {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Display title; empty string to display the model's file name

Remarks

This property works like the FeatureManager design tree **RMB > Rename tree item**.

To get the display title of lightweight assembly components, use [IComponent2::DisplayTitle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~DisplayTitle.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[DAssemblyDocEvents\_RenameDisplayTitleNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RenameDisplayTitleNotifyEventHandler.md)  
[DDrawingDocEvents\_RenameDisplayTitleNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_RenameDisplayTitleNotifyEventHandler.md)  
[DPartDocEvents\_RenameDisplayTitleNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_RenameDisplayTitleNotifyEventHandler.md)
