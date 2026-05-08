# SaveAsPreviousVersion Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~SaveAsPreviousVersion`

Sets the SOLIDWORKS version to save to.
Sets the SOLIDWORKS version to save to.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

WriteOnly Property SaveAsPreviousVersion As System.Integer
```

```

Dim instance As IAdvancedSaveAsOptions
 
instance.SaveAsPreviousVersion = value
```

```

System.int SaveAsPreviousVersion {set;}
```

```

property System.int SaveAsPreviousVersion {
   void set (    System.int value);
}
```

#### Property Value

SOLIDWORKS version to save to (see **Remarks**)

Remarks

Examine the Remarks of [ISldWorks::VersionHistory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~VersionHistory.md) to find the SOLIDWORKS version to save to.

For this property to save a model as a previous version, you must also use [IAdvancedSaveAsOptions::ModifyItemsNameAndPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~ModifyItemsNameAndPath.md) to change the name/path of all of the model's references. You must provide a different name/path than the current name/path, otherwise the SaveAs operation may fail because overwriting the same file is not supported.

Example

See the [IAdvancedSaveAsOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAdvancedSaveAsOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.md)  
[IAdvancedSaveAsOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.md)
