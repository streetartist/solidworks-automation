# ShowInDocumentType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup~ShowInDocumentType`

Gets or sets the types of documents to show this CommandGroup.
Gets or sets the types of documents to show this CommandGroup.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowInDocumentType As System.Integer
```

```

Dim instance As ICommandGroup
Dim value As System.Integer
 
instance.ShowInDocumentType = value
 
value = instance.ShowInDocumentType
```

```

System.int ShowInDocumentType {get; set;}
```

```

property System.int ShowInDocumentType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Types of documents in which to show this CommandGroup as defined in [swDocTemplateTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocTemplateTypes_e.html)

Remarks

This method only affects menus. The toolbar for the CommandGroup will be visible in every context, i.e., none, part, assembly, or drawing.

Example

[Create Submenus in the CommandManager (C#)](Create_Submenus_in_the_CommandManager_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICommandGroup Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup.md)  
[ICommandGroup Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICommandGroup_members.md)
