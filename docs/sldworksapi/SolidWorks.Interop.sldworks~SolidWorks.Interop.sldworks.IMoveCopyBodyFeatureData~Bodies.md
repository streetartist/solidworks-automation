# Bodies Property (IMoveCopyBodyFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~Bodies`

Gets or sets the bodies to move or rotate and copy.
Gets or sets the bodies to move or rotate and copy.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Bodies As System.Object
```

```

Dim instance As IMoveCopyBodyFeatureData
Dim value As System.Object
 
instance.Bodies = value
 
value = instance.Bodies
```

```

System.object Bodies {get; set;}
```

```

property System.Object^ Bodies {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) to move or rotate and copy

Remarks

Use:

- [IMoveCopyBodyFeatureData::Copy](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~Copy.md) to get whether to copy the bodies
- [IMoveCopyBodyFeatureData::TransformType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~TransformType.md) to get whether to move or rotate the bodies

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Example

[Set Bodies for Move/Copy (C#)](Set_Bodies_for_Move_Copy_Example_CSharp.htm)  
[Set Bodies for Move/Copy (VB.NET)](Set_Bodies_for_Move_Copy_Example_VBNET.htm)  
[Set Bodies for Move/Copy (VBA)](Set_Bodies_for_Move_Copy_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.md)  
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.md)  
[IMoveCopyBodyFeatureData::GetBodiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~GetBodiesCount.md)  
[IMoveCopyBodyFeatureData::IGetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~IGetBodies.md)  
[IMoveCopyBodyFeatureData::ISetBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~ISetBodies.md)
