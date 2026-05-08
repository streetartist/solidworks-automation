# GetArrowHeadInfo Method (IGtol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetArrowHeadInfo`

Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line.
Gets an array of doubles that describe the geometry of the arrowhead on the far end of the leader line.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetArrowHeadInfo() As System.Object
```

```

Dim instance As IGtol
Dim value As System.Object
 
value = instance.GetArrowHeadInfo()
```

```

System.object GetArrowHeadInfo()
```

```

System.Object^ GetArrowHeadInfo(); 
```

#### Return Value

Array (see **Remarks**)

Remarks

This information returned by this method is independent of whether this note actually has an arrowhead.

The format of the return value is the following array of doubles:

retval[0] = Arrow length (for example, leader into arrowhead)

retval[1] = Arrowhead length

retval[2] = Arrowhead width

retval[3] = Arrowhead style as defined in [swArrowStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swArrowStyle_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::GetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetArrowHeadAtIndex.md)  
[IGtol::GetArrowHeadCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetArrowHeadCount.md)  
[IGtol::IGetArrowHeadAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetArrowHeadAtIndex.md)  
[IGtol::IGetArrowHeadInfo Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetArrowHeadInfo.md)
