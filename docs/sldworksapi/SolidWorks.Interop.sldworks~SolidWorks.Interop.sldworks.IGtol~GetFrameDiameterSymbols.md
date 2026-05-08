# GetFrameDiameterSymbols Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameDiameterSymbols`

Gets whether diameter symbols are displayed for the specified frame.
Gets whether diameter symbols are displayed for the specified frame.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFrameDiameterSymbols( _
   ByVal FrameNumber As System.Short _
) As System.Object
```

```

Dim instance As IGtol
Dim FrameNumber As System.Short
Dim value As System.Object
 
value = instance.GetFrameDiameterSymbols(FrameNumber)
```

```

System.object GetFrameDiameterSymbols( 
   System.short FrameNumber
)
```

```

System.Object^ GetFrameDiameterSymbols( 
   System.short FrameNumber
) 
```

#### Parameters

*FrameNumber*
:   Frame number to examine (1 or 2)

#### Return Value

Array (see **Remarks**)

Remarks

This method is valid only if this Gtol was created in a version of SOLIDWORKS earlier than 2022.

The return value should be an array of two Booleans, with the following format:

*retval*[0] = True if the first tolerance value has a diameter symbol, false if it does not

*retval*[1] = True if the second tolerance value has a diameter symbol, false if it does not

Use this method in combination with [IGtol::GetFrameSymbols2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameSymbols2.md) that is used to retrieve the frame symbols.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::GetFrameCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameCount.md)  
[IGtol::GetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameSymbols2.md)  
[IGtol::GetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetFrameValues.md)  
[IGtol::IGetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameSymbols2.md)  
[IGtol::IGetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetFrameValues.md)  
[IGtol::SetFrameSymbols2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameSymbols2.md)  
[IGtol::SetFrameValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameValues.md)
