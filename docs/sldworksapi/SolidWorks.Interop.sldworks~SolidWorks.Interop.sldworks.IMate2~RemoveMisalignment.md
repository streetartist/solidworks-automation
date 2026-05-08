# RemoveMisalignment Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~RemoveMisalignment`

Removes the misaligned mate condition of this concentric mate.
Removes the misaligned mate condition of this concentric mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function RemoveMisalignment() As System.Boolean
```

```

Dim instance As IMate2
Dim value As System.Boolean
 
value = instance.RemoveMisalignment()
```

```

System.bool RemoveMisalignment()
```

```

System.bool RemoveMisalignment(); 
```

#### Return Value

True if the misaligned mate condition is successfully removed, false if not

Remarks

After calling this method, one of the concentric mates may be unsolvable.

Example

```

'VBA
```

```

'Open an assembly with a misaligned concentric mate, Concentric1
```

```

Dim swfeature As SldWorks.Feature  
Dim swmate As SldWorks.Mate2  
Sub main()
```

```

    Set swApp = Application.SldWorks  
    Set swassm = swApp.ActiveDoc  
    Set Swfeat = swassm.FeatureByName("Concentric1")  
    Set swmate = Swfeat.GetSpecificFeature2  
    Debug.Print "Concentric mate type as defined in swConcentricAlignmentType_e: " & swmate.GetConcentricAlignmentType  

```

```

    'Remove the misaligned mate condition  
    swmate.RemoveMisalignment  
    
```

```

    'Create the misaligned mate condition  
    swmate.ForceMisalignment
```

```

End Sub
```

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)  
[IMate2::ForceMisalignment Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~ForceMisalignment.md)
