# Copy Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~Copy`

Gets or sets whether to copy the selected bodies.
Gets or sets whether to copy the selected bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Copy As System.Boolean
```

```

Dim instance As IMoveCopyBodyFeatureData
Dim value As System.Boolean
 
instance.Copy = value
 
value = instance.Copy
```

```

System.bool Copy {get; set;}
```

```

property System.bool Copy {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to copy the selected bodies, false to not

Remarks

To get or set the number of copies of the selected bodies to create, call [IMoveCopyBodyFeatureData::NumberOfCopies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData~NumberOfCopies.md).

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMoveCopyBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData.md)  
[IMoveCopyBodyFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveCopyBodyFeatureData_members.md)
