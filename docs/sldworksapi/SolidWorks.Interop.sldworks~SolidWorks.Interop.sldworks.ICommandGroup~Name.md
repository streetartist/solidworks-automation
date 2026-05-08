# Name Property (ICommandGroup)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~Name`

Gets the name of the CommandGroup.
Gets the name of the CommandGroup.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Name As System.String
```

```

Dim instance As ICommandGroup
Dim value As System.String
 
value = instance.Name
```

```

System.string Name {get;}
```

```

property System.String^ Name {
   System.String^ get();
}
```

#### Property Value

Name of the CommandGroup that corresponds to the name specified in [ICommandManager::AddContextMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~AddContextMenu.md),  
and [ICommandManager::CreateCommandGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~CreateCommandGroup.md).

Remarks

If you used [ICommandManager::GetGroups](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~GetGroups.md) or [ICommandManager::IGetGroups](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandManager~IGetGroups.md), then use this property to get the specific CommandGroup with which you want to work.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md)  
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.md)
