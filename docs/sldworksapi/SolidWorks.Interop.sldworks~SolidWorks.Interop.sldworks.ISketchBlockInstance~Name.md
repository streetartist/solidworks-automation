# Name Property (ISketchBlockInstance)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance~Name`

Gets or sets the name of this block instance.
Gets or sets the name of this block instance.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Name As System.String
```

```

Dim instance As ISketchBlockInstance
Dim value As System.String
 
instance.Name = value
 
value = instance.Name
```

```

System.string Name {get; set;}
```

```

property System.String^ Name {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Name of this block instance

Remarks

After setting the name of a block instance, use [IFeatureManager::UpdateFeatureTree](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~UpdateFeatureTree.md) to see its name in the FeatureManager design tree.

Example

[Get and Set Blocks Data in Any Document (VBA)](Get_and_Set_Blocks_Data_in_Any_Document_Example_VB.htm)  
[Get Block Information (VBA)](Get_Block_Information_Example_VB.htm)  
[Get Blocks in Drawing (VBA)](Get_Blocks_in_Drawing_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchBlockInstance Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance.md)  
[ISketchBlockInstance Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockInstance_members.md)
