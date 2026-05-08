# CommandInProgress Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CommandInProgress`

Improves performance of out-of-process applications by informing SOLIDWORKS that a sequence of API calls will be made by the out-of-process application.
Improves performance of out-of-process applications by informing SOLIDWORKS that a sequence of API calls will be made by the out-of-process application.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CommandInProgress As System.Boolean
```

```

Dim instance As ISldWorks
Dim value As System.Boolean
 
instance.CommandInProgress = value
 
value = instance.CommandInProgress
```

```

System.bool CommandInProgress {get; set;}
```

```

property System.bool CommandInProgress {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

Set to True before calling the sequence of API calls, then set to false after calling the sequence of API calls

Remarks

SOLIDWORKS then reduces the number of updates it makes during these calls. Use of this property only effects out-of-process applications.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
