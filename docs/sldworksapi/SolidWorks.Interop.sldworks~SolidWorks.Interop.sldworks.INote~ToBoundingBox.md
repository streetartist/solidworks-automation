# ToBoundingBox Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~ToBoundingBox`

Gets and sets whether to select the To bounding box option for leaders in this note's PropertyManager page.
Gets and sets whether to select the **To bounding box** option for leaders in this note's PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ToBoundingBox As System.Boolean
```

```

Dim instance As INote
Dim value As System.Boolean
 
instance.ToBoundingBox = value
 
value = instance.ToBoundingBox
```

```

System.bool ToBoundingBox {get; set;}
```

```

property System.bool ToBoundingBox {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to select the **To bounding box** option, false to not

Remarks

See the SOLIDWORKS Help for information about the **To bounding box** option.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)
