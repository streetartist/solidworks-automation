# FileName Property (ISketchBlockDefinition)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~FileName`

Gets or sets the name of the file to which }}-->the block definition is linked.
Gets or sets the name of the file to which the block definition is linked.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FileName As System.String
```

```

Dim instance As ISketchBlockDefinition
Dim value As System.String
 
instance.FileName = value
 
value = instance.FileName
```

```

System.string FileName {get; set;}
```

```

property System.String^ FileName {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Path and filename of the block definition file

Remarks

The file can be either a native SOLIDWORKS block file (.sldblk) or a non-native SOLIDWORKS file (.dxf or .dwg).

This method gets the name of the file with which this block definition is associated, regardless of whether or not the link is enabled. SOLIDWORKS continues to store the name of the file if the link is disabled. Use [ISketchBlockDefintion::LinkToFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~LinkToFile.md) to determine if the block definition is linked to a file.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md)  
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.md)  
[ISketchBlockDefinition::Save Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~Save.md)
