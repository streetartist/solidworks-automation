# ToolboxPartType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ToolboxPartType`

Gets and sets whether this part is a SOLIDWORKS Toolbox part.
Gets and sets whether this part is a SOLIDWORKS Toolbox part.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ToolboxPartType As System.Integer
```

```

Dim instance As IModelDocExtension
Dim value As System.Integer
 
instance.ToolboxPartType = value
 
value = instance.ToolboxPartType
```

```

System.int ToolboxPartType {get; set;}
```

```

property System.int ToolboxPartType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of SOLIDWORKS Toolbox part type as defined in [swToolBoxPartType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swToolBoxPartType_e.html)

Example

[Test for Toolbox Part (VBA)](Test_For_Toolbox_Part_Example_VB.htm)  
[Test for Toolbox Part (VB.NET)](Test_for_Toolbox_Part_Example_VBNET.htm)  
[Test for Toolbox Part (C#)](Test_for_Toolbox_Part_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
