# TriadRotationParameters Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~TriadRotationParameters`

Gets or sets the rotation parameters for this Move Face feature.
Gets or sets the rotation parameters for this Move Face feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TriadRotationParameters As System.Object
```

```

Dim instance As IMoveFaceFeatureData
Dim value As System.Object
 
instance.TriadRotationParameters = value
 
value = instance.TriadRotationParameters
```

```

System.object TriadRotationParameters {get; set;}
```

```

property System.Object^ TriadRotationParameters {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of six doubles (see **Remarks**)

Remarks

The first three doubles are the X, Y, and Z rotation origin parameters. The remaining three doubles are the X, Y, and Z rotation angle parameters.

Example

[Rotate Move Face Feature (VB.NET)](Rotate_Move_Face_Feature_Example_VBNET.htm)  
[Rotate Move Face Feature (VBA)](Rotate_MoveFace_Feature_Example_VB.htm)  
[Rotate Move Face Feature (C#)](Rotate_Move_Face_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.md)  
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.md)  
[IMoveFaceFeatureData::IGetTriadRotationParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~IGetTriadRotationParameters.md)  
[IMoveFaceFeatureData::ISetTriadRotationParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~ISetTriadRotationParameters.md)
