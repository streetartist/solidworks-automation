# LeaderAttachmentToFaces Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~LeaderAttachmentToFaces`

Gets and sets whether to attach balloons to faces.
Gets and sets whether to attach balloons to faces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LeaderAttachmentToFaces As System.Boolean
```

```

Dim instance As IAutoBalloonOptions
Dim value As System.Boolean
 
instance.LeaderAttachmentToFaces = value
 
value = instance.LeaderAttachmentToFaces
```

```

System.bool LeaderAttachmentToFaces {get; set;}
```

```

property System.bool LeaderAttachmentToFaces {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to attach balloons to faces; false to attach balloons to edges

Remarks

See the SOLIDWORKS Help for additional details about autoballoons.

Example

See [IAutoBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.md)  
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.md)
