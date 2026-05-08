# AddToDB Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~AddToDB`

Gets or sets whether sketch entities are added directly to the SOLIDWORKS database.
Gets or sets whether sketch entities are added directly to the SOLIDWORKS database.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AddToDB As System.Boolean
```

```

Dim instance As ISketchManager
Dim value As System.Boolean
 
instance.AddToDB = value
 
value = instance.AddToDB
```

```

System.bool AddToDB {get; set;}
```

```

property System.bool AddToDB {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to add items directly to the SOLIDWORKS database, false to not

Remarks

One of the benefits of adding sketch entities directly to the database is that you can avoid grid and entity snapping. For example, if you create a sketch line whose endpoint is near another entity or grid point, the new sketch line endpoint snaps to the other entity or grid point. Setting this property to true avoids this behavior during sketch entity creation.

After setting this property to true:

- It is not possible to undo the creation of some types of sketch entities.
- You must reset it to false to restore SOLIDWORKS' normal operating mode.

This property and [ISketchManager::DisplayWhenAdded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~DisplayWhenAdded.md) improve performance during sketch entity creation. ISketchManager::DisplayWhenAdded requires that this property be set to true.

If you want to constrain all the sketch entities after creation, use [ISketch::ConstrainAll](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~ConstrainAll.md).

Example

[Get Assembly Bounding Box Using Components (C#)](Get_Assembly_Bounding_Box_Using_Components_Example_CSharp.htm)  
[Get Assembly Bounding Box Using Components (VB.NET)](Get_Assembly_Bounding_Box_Using_Components_Example_VBNET.htm)  
[Get Assembly Bounding Box Using Components (VBA)](Get_Assembly_Bounding_Box_using_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.md)  
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.md)
