# TreeDisplay Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager~TreeDisplay`

Gets the organization of the DimXpertManager tab information: by annotation, by features, or flat.
Gets the organization of the DimXpertManager tab information:  by annotation, by features, or flat.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TreeDisplay As System.Integer
```

```

Dim instance As IDimXpertManager
Dim value As System.Integer
 
instance.TreeDisplay = value
 
value = instance.TreeDisplay
```

```

System.int TreeDisplay {get; set;}
```

```

property System.int TreeDisplay {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of tree display as defined in [swDimXpertTreeDisplay\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDimXpertTreeDisplay_e.html)

Remarks

This property corresponds to a Tree Display menu item when the right-mouse-button is clicked on a schema in the DimXpertManager tab.

Example

[Get DimXpertManager Info (VBA)](Get_DimXpertManager_Info_Example_VB.htm)  
[Get DimXpertManager Info (VB.NET)](Get_DimXpertManager_Info_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimXpertManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager.md)  
[IDimXpertManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager_members.md)
