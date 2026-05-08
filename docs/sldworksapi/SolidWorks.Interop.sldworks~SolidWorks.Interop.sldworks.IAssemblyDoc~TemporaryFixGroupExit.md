# TemporaryFixGroupExit Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~TemporaryFixGroupExit`

Changes components that were temporarily fixed or grouped back to floating or ungrouped after such operations as drag, move, rotate, etc.
Changes components that were temporarily fixed or grouped back to floating or ungrouped after such operations as drag, move, rotate, etc.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub TemporaryFixGroupExit() 
```

```

Dim instance As IAssemblyDoc
 
instance.TemporaryFixGroupExit()
```

```

void TemporaryFixGroupExit()
```

```

void TemporaryFixGroupExit(); 
```

Remarks

To temporarily change floating or ungrouped components to fixed or grouped, call [IAssemblyDoc::TemporaryFixGroup](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~TemporaryFixGroup.md).

Example

[Temporarily Fix and Group Components (C#)](Temporarily_Fix_and_Group_Components_Example_CSharp.htm)  
[Temporarily Fix and Group Components (VB.NET)](Temporarily_Fix_and_Group_Components_Example_VBNET.htm)  
[Temporarily Fix and Group Components (VBA)](Temporarily_Fix_and_Group_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IComponent2::IsFixed Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsFixed.md)  
[IAssemblyDoc::FixComponent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~FixComponent.md)  
[IAssemblyDoc::UnfixComponent Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~UnfixComponent.md)
