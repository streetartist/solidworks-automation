# LinkToFile Property (ISketchBlockDefinition)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~LinkToFile`

Gets or sets whether the block definition file is linked to a file.
Gets or sets whether the block definition file is linked to a file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LinkToFile As System.Boolean
```

```

Dim instance As ISketchBlockDefinition
Dim value As System.Boolean
 
instance.LinkToFile = value
 
value = instance.LinkToFile
```

```

System.bool LinkToFile {get; set;}
```

```

property System.bool LinkToFile {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the block definition is linked to a file, false if not

Remarks

The file can be either a native SOLIDWORKS block file (.sldblk) or a non-native SOLIDWORKS file (.dxf or .dwg).

This property indicates whether the block definition is linked to an external file, which you can enable or disable on the block definition without destroying the file name. That is, the file name continues to be stored even if the link is disabled.

Use [ISketchBlockDefinition::FileName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~FileName.md) to get the name of the file to which a block definition is linked.

You can link a block definition to a .sldblk file. However, you cannot save a block definition to a .sldblk file by only calling SketchBlockDefinition::FileName (True) and SketchBlockDefinition::LinkToFile (Filename). You must first either save the block by selecting it and calling [ISketchBlockDefinition::Save](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~Save.md), or you can assign the block to an already existing .sldblk file.

Example

[Get and Set Blocks in Any Document (VBA)](Get_and_Set_Blocks_Data_in_Any_Document_Example_VB.htm)  
[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.md)  
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.md)  
[ISketchBlockDefinition::MakeSketchBlockFromFile Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromFile.md)  
[ISketchBlockDefinition::MakeSketchBlockFromSelected Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSelected.md)  
[ISketchBlockDefinition::MakeSketchBlockFromSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~MakeSketchBlockFromSketch.md)
