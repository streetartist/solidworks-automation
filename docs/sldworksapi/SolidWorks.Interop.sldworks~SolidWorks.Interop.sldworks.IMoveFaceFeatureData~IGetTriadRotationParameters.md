# IGetTriadRotationParameters Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~IGetTriadRotationParameters`

Gets the rotation parameters for this Move Face feature.
Gets the rotation parameters for this Move Face feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetTriadRotationParameters() As System.Double
```

```

Dim instance As IMoveFaceFeatureData
Dim value As System.Double
 
value = instance.IGetTriadRotationParameters()
```

```

System.double IGetTriadRotationParameters()
```

```

System.double IGetTriadRotationParameters(); 
```

#### Return Value

- in-process, unmanaged C++: Pointer to an array of six doubles (see **Remarks**)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The first three doubles returned are the X, Y, and Z rotation origin parameters. The remaining three doubles returned are the X, Y, and Z rotation angle parameters.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.md)  
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.md)  
[IMoveFaceFeatureData::ISetTriadRotationParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~ISetTriadRotationParameters.md)  
[IMoveFaceFeatureData::TriadRotationParameters Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~TriadRotationParameters.md)
