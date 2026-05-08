# Faces Property (ISMNormalCutGroupData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutGroupData~Faces`

Gets or sets the cut-extrude faces in this group.
Gets or sets the cut-extrude faces in this group.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Faces As System.Object
```

```

Dim instance As ISMNormalCutGroupData
Dim value As System.Object
 
instance.Faces = value
 
value = instance.Faces
```

```

System.object Faces {get; set;}
```

```

property System.Object^ Faces {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Example

See the [ISMNormalCutFeatureData2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutFeatureData2.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMNormalCutGroupData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutGroupData.md)  
[ISMNormalCutGroupData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMNormalCutGroupData_members.md)
